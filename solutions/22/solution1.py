
import re

from copy import deepcopy
def sort_by_z():
    return sorted(cubes, key=lambda x: x.z2)

class Cube():
    def __init__(self, numbers, name) -> None:
        self.x1 = numbers[0]
        self.y1 = numbers[1]
        self.z1 = numbers[2]
        self.x2 = numbers[3]
        self.y2 = numbers[4]
        self.z2 = numbers[5]
        self.items = []
        self.name = name
        for x in range(self.x1, self.x2+1):
            for y in range(self.y1, self.y2+1):
                for z in range(self.z1, self.z2+1):
                    self.items.append((x,y,z))
        
cubes = []

def move_single_cube_down(cube, cube_list, offset=0):

    if cube.z1 == 0:
        return cube
    items = [(x, y, z-1) for x, y, z in cube.items]

    for c in cube_list:
        if c != cube:
            for i in items:
                if i in c.items:
                    # clash...
                    return cube
    
    cube.z1 -= 1
    cube.z2 -= 1
    cube.items = items
    if cube.z1 == 0:
        return cube
    return move_single_cube_down(cube, cube_list, offset)
            



def move_cubes_down(cube_list, exclude=-1):
    results = 0
    for i in range(0, len(cube_list)):
        #print(i)
        if i == exclude:
            continue
        z1 = cube_list[i].z1
        cube_list[i] = move_single_cube_down(cube_list[i],  cube_list, i)
        if cube_list[i].z1 != z1:
            results += 1
    return results

with open("data.txt") as f:
    lines = f.read().split("\n")
    mx = my = mz = 0
    uid = 0
    for l in lines:
        numbers = [int(i) for i in re.findall("\d+", l)]
        print(numbers)
        cubes.append(Cube(numbers, chr(uid+ord("a"))))
        mx = max(cubes[-1].x1, cubes[-1].x2, mx)
        my = max(cubes[-1].y1, cubes[-1].y2, my)
        mz = max(cubes[-1].z1, cubes[-1].z2, mz)

        uid = (uid + 1) % 26
        
    cubes = sort_by_z()
    for c in cubes:
        print(vars(c))
    print(mx, my, mz)
    # for i in range(1):
    #     print(i)
    
    #move_single_cube_down(cubes[0])
    moves = move_cubes_down(cubes)
    print("-->", moves)


    possible_to_remove = 0
    part2 = 0
    for i in range(len(cubes)):
        temp_list = deepcopy(cubes)
        temp_list.pop(i) 
        moves = move_cubes_down(temp_list)
        part2 += moves
        if not moves:
            
            possible_to_remove += 1

        print(i, "-->", moves)
    
    print("result", possible_to_remove, part2)

    # for z in range(0, mz+1):
    #     print("layer..", z)
    #     for y in range(0, my+1):
    #         for x in range(0, mx+1):
    #             sym = '.'
    #             for c in cubes:
    #                 if (x,y,z) in c.items:
    #                     sym = c.name
    #                     break
    #             print(sym, end="")
    #         print("")
    #     print("\n\n")

    # cubes are now down.
    # we can remove the cube and rerun our stack.


#    move_cubes_down()