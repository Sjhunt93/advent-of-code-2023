#from termcolor import colored
import itertools
from copy import deepcopy

# I could never get this to work :(())

class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.distance = 0 #g
        self.estimatedDis = 0 #h
        self.cost = 0 #f
        self.st_cost = [0, 0] # special case
        self.lava = 0
        self.direction = [0,0]

    def __eq__(self, other):
        return self.position == other.position and self.direction == other.direction# and self.cost == other.cost


def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    visited = set()
    # Create start and end node
    start_node = Node(None, start)
    start_node.distance = start_node.estimatedDis = start_node.cost = 0
    end_node = Node(None, end)
    end_node.distance = end_node.estimatedDis = end_node.cost = 0
    start_node.lava = 2
    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)
    results = []
    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, node in enumerate(open_list):
            if node.cost < current_node.cost:
                current_node = node
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)
        #print("closing:", vars(current_node))
        # Found the goal
        if current_node.position == end_node.position:
            print("hit end")
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            #return path[::-1] # Return reversed path
            results.append(path[::-1])

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]: # Adjacent squares
            
            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
            #print(current_node.position, node_position)
            st_cost = list(current_node.st_cost)
            if current_node.position[0] == node_position[0]: # and (st_cost[0] > 0 or st_cost[1] > 0): # is moving X
                if st_cost[1] > 0: # was moving y
                    st_cost = [1, 0]
                else:
                    st_cost[0] += 1
            elif current_node.position[1] == node_position[1]:
                if st_cost[0] > 0: # was moving x
                    st_cost = [0, 1]
                else:
                    st_cost[1] += 1
            
            # Make sure within range
            if tuple([node_position[0], node_position[1], new_position[0], new_position[1], current_node.cost]) in visited:
                continue
                

            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue
            if st_cost[0] >= 3 or st_cost[1] >= 3: #special rule here for 3 in a line..
                continue

    

            # Create new node
            new_node = Node(current_node, node_position)
            new_node.st_cost = list(st_cost)
            new_node.lava = int(matrix[node_position[1]][node_position[0]])
            new_node.direction = new_position
            # Append
            children.append(new_node)
            visited.add(tuple([node_position[0], node_position[1], new_position[0], new_position[1], current_node.cost]))

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    #print("Ignoring:", vars(child))
                    continue

            # Create the f, g, and h values
            child.distance = current_node.distance + 1
            child.estimatedDis = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            t = child.parent
            c = 0
            while t is not None:
                c += t.lava
                t = t.parent
            #print(c)
            child.cost = 0# child.distance + child.estimatedDis + c#  + c*3# child.distance + child.estimatedDis
            #child.cost = current_node.lava  + child.estimatedDis + child.distance#int(matrix[child.position[1]][child.position[0]])# + child.distance + child.estimatedDis
            #child.lava += current_node.lava
            # Child is already in the open list
            # for open_node in open_list:
            #     if child == open_node and child.distance > open_node.distance:
            #         continue

            # Add the child to the open list
            open_list.append(child)

    return results

def to_matrix(lines):
    items = []
    for l in lines:
        #print(l)
        items.append([i for i in l])
    return items

# HELPER
#print(hscore, vscore)
# for y, row in enumerate(matrix):
#     print(row)
#     for x, col in enumerate(row):
#         c = matrix[y][x]


with open("data.txt") as f:

    lines = f.read().split("\n")
    matrix = to_matrix(lines)

    start = (0, 0)
    end = (len(matrix[0])-1, len(matrix)-1)

    paths = astar(matrix, start, end)
    
    print(paths)
    
    for path in paths:
        cost = 0
        for p in path:
            cost += int(matrix[p[1]][p[0]])
            #matrix[p[1]][p[0]] = "#"
        print(path, cost)

    # for r in matrix:
    #     print(''.join([i for i in r]))
    # print("\n")

    