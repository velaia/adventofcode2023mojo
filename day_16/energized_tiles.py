import numpy as np
import itertools


"""
Idea: solve the puzzle using recursion.

Stopping condition: outside of width/height boundaries of the map
For each step yield the position and set to True/1 in a np.array of the same size.
At correctly placed splitters: recursively create "subthreads"
"""

filename = "input.txt"
input = []
with open(filename, "r") as input_file:
    for line in input_file.readlines():
        input.append(line.strip())

height, width = len(input), len(input[0])
energized_locations = np.zeros((height, width))
energized_locations_directions = []

def initialize_locations_and_directions():
    global energized_locations, energized_locations_directions
    energized_locations = np.zeros((height, width))
    energized_locations_directions = []
    for i, line in enumerate(input):
        energized_locations_directions.append([])
        for j, char in enumerate(line):
            energized_locations_directions[i].append([])

reflection_map = {
    "\\": {
        1: -2,
        2: -1,
        -1: 2,
        -2: 1
    },
    "/": {
        1: 2,
        2: 1,
        -2: -1,
        -1: -2
    }
}

# recursion was going to deep so shifted to this "job queue"
trace_light_queue = []
def calculate(input):
    initialize_locations_and_directions()

    energized_tiles_list = []
    for i in range(width):
        energized_tiles_list.append(calculate_one_entry(((-1, i), -2)))
        energized_tiles_list.append(calculate_one_entry(((height, i), 2)))
    
    for i in range(height):
        energized_tiles_list.append(calculate_one_entry(((i, -1), 1)))
        energized_tiles_list.append(calculate_one_entry(((i, width), -1)))
    
    return max(energized_tiles_list)

def calculate_one_entry(entry):
    global trace_light_queue, energized_locations
    trace_light_queue = []
    trace_light_queue.append(entry)
    try:
        while next_pos := trace_light_queue.pop(0):
            trace_light(next_pos[0], next_pos[1])
    except:
        result = np.sum(energized_locations == 1)
        # reset map
        initialize_locations_and_directions()
        return result

def trace_light(current_pos, direction):
    global width, height, input, energized_locations, trace_light_queue


    """direction:left, right: -1, 1; down, up: -2, +2"""
    if direction == 1:
        new_pos = (current_pos[0], current_pos[1] + 1)
    elif direction == -1:
        new_pos = (current_pos[0], current_pos[1] - 1)
    elif direction == 2:
        new_pos = (current_pos[0] - 1, current_pos[1])
    elif direction == -2:
        new_pos = (current_pos[0] + 1, current_pos[1])
    
    # base case stopping condition
    if new_pos[0] >= height or new_pos[0] < 0 or new_pos[1] >= width or new_pos[1] < 0:
        # outside of bounds, return 0
        return 0
    
    # check if location has already been hit by light going in this direction
    energized_locations[new_pos[0]][new_pos[1]] = 1
    if direction in energized_locations_directions[new_pos[0]][new_pos[1]]:
        return 0
    else: energized_locations_directions[new_pos[0]][new_pos[1]].append(direction)
    
    new_pos_sym = input[new_pos[0]][new_pos[1]]

    if new_pos_sym == ".":
        trace_light_queue.append((new_pos, direction))
    elif new_pos_sym == "|":
        if direction in (1, -1):
            trace_light_queue.append((new_pos, 2))
            trace_light_queue.append((new_pos, -2))
        else:
            trace_light_queue.append((new_pos, direction))
    elif new_pos_sym == "-":
        if direction in (2, -2):
            trace_light_queue.append((new_pos, 1))
            trace_light_queue.append((new_pos, -1))
        else:
            trace_light_queue.append((new_pos, direction))
    else:
        # \ or /
        new_direction = reflection_map.get(new_pos_sym).get(direction)
        trace_light_queue.append((new_pos, new_direction))


print(f"result: {calculate(input)}")