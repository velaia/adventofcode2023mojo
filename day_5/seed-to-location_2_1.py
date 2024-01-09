
import numpy as np

dev = ("input_sample.txt", ((3,4),
    (7,9),
    (12, 15),
    (18, 19),
    (22, 24),
    (27, 28),
    (31, 32)))
prod = ("input.txt", ((3, 14),
    (17, 45),
    (48, 75),
    (78, 96),
    (99, 134),
    (137, 160),
    (163, 182)))

input_params = prod
inputs = open(input_params[0], "r")
input_lines = inputs.readlines()
inputs.close()
mappings = []

seeds_ranges_coordinates = [int(start_stop) for start_stop in input_lines[0].split()[1:]]
seed_ranges = sum([seeds_ranges_coordinates[i+1] for i in range(0, len(seeds_ranges_coordinates), 2)])
print(f"number of initial seeds: {seed_ranges}")
seed_ranges = [range(seeds_ranges_coordinates[i], seeds_ranges_coordinates[i] + seeds_ranges_coordinates[i+1], 1) for i in range(0, len(seeds_ranges_coordinates), 2)]
print(seed_ranges)



def get_mapping_for_lines(start_line: int, finish_line: int):
    mapping = []
    destination_range_starts = []
    source_range_starts = []
    range_lengths = []
    for entry in [line.split() for line in input_lines[start_line:finish_line + 1]]:
        destination_range_starts.append(int(entry[0]))
        source_range_starts.append(int(entry[1]))
        range_lengths.append(entry[2])
        # mapping.append({"source_range_start": source_range_start, "destination_range_start": destination_range_start, "range_length": range_length})
    
    max_col2_idx = np.argmax(source_range_starts)
    max_col1_idx = np.argmax(destination_range_starts)
    print(f"input range boundaries (incl): [{min(source_range_starts)} : {max(source_range_starts) + int(range_lengths[max_col2_idx])}] \
          and output range boundaries (incl): [{min(destination_range_starts)} : {max(destination_range_starts) + int(range_lengths[max_col1_idx]) }]")
    return mapping

mappings = [get_mapping_for_lines(start, stop) for start,stop in 
    input_params[1]]

min_loc_seed = None
min_location_number = 100_000_000_000
min_path_step_number = 100_000_000_000
max_path_step_number = 0
counter = 0
all_paths = []
# for seeds in seed_ranges:
#     for seed in seeds:
#         counter += 1
#         # if counter % 10_000 == 0:
#         #     # print("another 1,000,000")
#         #     print(f"min loc number: {min_location_number:,}, responsible seed: {min_loc_seed:,}, {max_path_step_number = }, {min_path_step_number =}")
#         path = [seed,]
#         current_seed = seed
#         for mapping in mappings:
#             prev_seed = current_seed
#             for source_range in mapping:
#                 # print(f"mapping details: { source_range['destination_range_start']:_}, {source_range['source_range_start']:_}, {source_range['range_length']:_}, dest_range+diff: {source_range['destination_range_start'] + (current_seed - source_range['source_range_start']):_}")
#                 if current_seed >= source_range['source_range_start'] and current_seed < source_range['source_range_start'] + source_range['range_length']:
#                     # print(f"{current_seed:_} is in source range { source_range['source_range_start']:_} to { source_range['source_range_start'] + source_range['range_length']:,}.")
#                     current_seed = source_range['destination_range_start'] + (current_seed - source_range['source_range_start'])
#                     # print(f"setting current_seed to new value: {current_seed:_}")
#                     break
#                 else:
#                     # print(f"{current_seed:,} is in not source range { source_range['source_range_start']:,} to { source_range['source_range_start'] + source_range['range_length']:,}.")
#                     pass
#                 # print("finished checking one mapping range with resulting")
#             # print(f"finished one mapping like seed -> soil, result {prev_seed:_} -> {current_seed:_}")
#             path.append(current_seed)
#         # print(f"finished seed {seed:_} with mapping-result: {current_seed:_}")
#         # print(" -> ".join([f"{step:,}" for step in path]))
#         # all_paths.extend(path)
#         max_path_step_number = max(max(path), max_path_step_number)
#         min_path_step_number = min(min(path), min_path_step_number)
#         prev_min_loc_number = min_location_number
#         min_location_number = min(current_seed, min_location_number)
#         if min_location_number < prev_min_loc_number:
#             min_loc_seed = seed


# print(f"{min_location_number:,}, responsible seed: {min_loc_seed:,}, {max_path_step_number = }, {min_path_step_number =}")
