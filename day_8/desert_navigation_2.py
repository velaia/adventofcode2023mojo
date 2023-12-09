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
    # all strings ending in A; ending in only nodes ending in z
    lookup, end = 'A', 'Z'

    for line in input.readlines():
        desert_map[line[0:3]] = line[7:-2].split(", ")
        map_locs.append(line[0:3])

    start_loc_idxs = np.argwhere(tuple(map(lambda x: x.endswith(lookup), map_locs)))
    end_loc_idxs = np.argwhere(tuple(map(lambda x: x.endswith(end), map_locs)))
    start_locs = [map_locs[x[0]] for x in start_loc_idxs.tolist()]
    end_locs = [map_locs[x[0]] for x in end_loc_idxs.tolist()]

    prev_locs = start_locs
    counter = 0
    for instr in instruction_generator(instructions):
        if counter < 200_000_000:
            new_locs = []
            for loc in prev_locs:
                # print(f"checking loc {loc}")
                new_locs.append(desert_map[loc][0 if instr == 'L' else 1])
            counter +=1
            
            if counter % 1_000_000 == 0:
                print(new_locs)

            new_loc_correct_ending = list([x.endswith(end) for x in  new_locs])
            if np.any(new_loc_correct_ending):
                print(f"{counter}: {new_loc_correct_ending}")
            if np.all(list([x.endswith(end) for x in  new_locs])):
                break
            prev_locs = new_locs
        else:
            break
    
    print(f"steps: {counter}")

