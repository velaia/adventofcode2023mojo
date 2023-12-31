
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

input_params = dev
inputs = open(input_params[0], "r")
input_lines = inputs.readlines()
inputs.close()
mappings = []

seeds = [int(seed) for seed in input_lines[0].split()[1:]]

def get_mapping_for_lines(start_line: int, finish_line: int):
    mapping = []
    for entry in [line.split() for line in input_lines[start_line:finish_line + 1]]:
        destination_range_start = int(entry[0])
        source_range_start = int(entry[1])
        range_length = int(entry[2])
        mapping.append({"source_range_start": source_range_start, "destination_range_start": destination_range_start, "range_length": range_length})
    return mapping

mappings = [get_mapping_for_lines(start, stop) for start,stop in 
    input_params[1]]

location_numbers = []
for seed in seeds:
    path = [seed,]
    # print(f"starting seed {seed:_}")
    current_seed = seed
    for mapping in mappings:
        prev_seed = current_seed
        for source_range in mapping:
            # print(f"mapping details: { source_range['destination_range_start']:_}, {source_range['source_range_start']:_}, {source_range['range_length']:_}, dest_range+diff: {source_range['destination_range_start'] + (current_seed - source_range['source_range_start']):_}")
            if current_seed >= source_range['source_range_start'] and current_seed < source_range['source_range_start'] + source_range['range_length']:
                # print(f"{current_seed:_} is in source range { source_range['source_range_start']:_} to { source_range['source_range_start'] + source_range['range_length']:,}.")
                current_seed = source_range['destination_range_start'] + (current_seed - source_range['source_range_start'])
                # print(f"setting current_seed to new value: {current_seed:_}")
                break
            else:
                # print(f"{current_seed:,} is in not source range { source_range['source_range_start']:,} to { source_range['source_range_start'] + source_range['range_length']:,}.")
                pass
            # print("finished checking one mapping range with resulting")
        # print(f"finished one mapping like seed -> soil, result {prev_seed:_} -> {current_seed:_}")
        path.append(current_seed)
    print(f"finished seed {seed:_} with mapping-result: {current_seed:_}")
    print(" -> ".join([f"{step:,}" for step in path]))
    location_numbers.append(current_seed)

print(f"{len(location_numbers) =}, {len(seeds) =}, minimum: {min(location_numbers):,}")