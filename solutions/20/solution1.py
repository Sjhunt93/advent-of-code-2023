

mapping = {

}

pulse_count = {
    0 : 0,
    1 : 0
}



class Node():
    pulse_count_plus = 0
    pulse_count_minus = 0

    def __init__(self, name, nodetype: str, outputs) -> None:
        if nodetype == "%":
            self.state = 0
        elif nodetype == "&":
            self.state = []

        self.inputs = [] # list of pulses
        self.name = name
        self.nodetype = nodetype
        self.outputs = [x.strip() for x in outputs]

    def trigger(self, pulse, input):
        if self.nodetype == "b":
            return [[self.name, o, pulse] for o in self.outputs]
        if self.nodetype == "%":
            
            if pulse == 0:
                self.state = not self.state
                return [[self.name, o, int(self.state)] for o in self.outputs]
            else:
                return []
        if self.nodetype == "&":
            
            self.state[input] = pulse
            n = int(sum(self.state.values()) != len(self.state.keys()))
            return [[self.name, o, n] for o in self.outputs]


def push_button():
    

    queue = []
    #queue.append(([["broadcaster", 0]], "button"))
    pulse_count[0] += 1
    queue.append([["button", "broadcaster", 0]])


    scanner = ["js", "zb", "bs", "rr"]
    while queue:
        instructions = queue.pop()

        next_step = []
        print("\n\n")
        for ins in instructions:
            print("dispatching --> ", ins)
            previous_output, input, pulse = ins
            #pulse_count[pulse] += 1
            if input in mapping:
                
                results = mapping[input].trigger(pulse, previous_output)
                
                print("returns <---- ", results)
                for r in results:
                    pulse_count[r[2]] += 1
                next_step += results
            elif input == 'rx' and pulse == 1:
                print("..")
        
        if next_step:
            queue.append(next_step)



with open("data.txt") as f:
    lines = f.read().split("\n")
    for l in lines:
        input, out = l[1:].split("->")
        if l[0] == '%':
            mapping[input.strip()] = Node(input.strip(), "%", out.split(","))
        elif l[0] == '&':
            mapping[input.strip()] = Node(input.strip(), "&", out.split(","))
        else:
            mapping["broadcaster"] = Node("b", "b", out.split(","))

    for key, node in mapping.items():

        inputs = []
        if node.nodetype == "&":
            for key2, node2 in mapping.items():
                if node.name in node2.outputs:
                    inputs.append(node2.name)
        
        node.state = {x:0 for x in inputs}


    for key, node in mapping.items():
        print(vars(node))

    for i in range(0, 1000):
        push_button(i)
    
    print(pulse_count)
    print(pulse_count[0] * pulse_count[1])