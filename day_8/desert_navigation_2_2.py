import numpy as np


dev = "input_sample_2.txt"
prod = "input.txt"
system = prod

def instruction_generator(instructions):
    counter = 0
    while True:
        next_instr = instructions[counter % len(instructions)]
        counter += 1
        yield next_instr


with open(system, "r") as input:
    instructions = input.readline().strip()
    input.readline()

    map_locs = []
    desert_map = {}
    # all strings ending in A; all strings must end in Z to finish
    lookup, end = 'A', 'Z'

    for pos, line in enumerate(input.readlines()):
        desert_map[line[0:3]] = line[7:-2].split(", ")
        map_locs.append(line[0:3])
    map_locs = np.array(map_locs)

    start_loc_idxs = np.argwhere([x.endswith(lookup) for x in map_locs]).flatten()

    loop_map = {}
    prev_locs = map_locs[start_loc_idxs]
    for num, instr in enumerate(instruction_generator(instructions)):
        new_locs = [desert_map[loc][0 if instr == 'L' else 1] for loc in prev_locs]
        new_loc_correct_ending = [x[-1] == end for x in  new_locs]

        if np.any(new_loc_correct_ending):
            loop_map[np.argmax(new_loc_correct_ending)] = min(num + 1, loop_map.get(np.argmax(new_loc_correct_ending), 1_000_000))
            if len(loop_map) == 6:
                break

        prev_locs = new_locs


    result = np.lcm.reduce(list(loop_map.values()))
    print(f"{result =}")
