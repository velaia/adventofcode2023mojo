dev = "input_sample.txt"
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

    desert_map = {}

    for line in input.readlines():
        desert_map[line[0:3]] = line[7:-2].split(", ")

    counter = 0
    lookup, end = 'AAA', 'ZZZ'
    for instr in instruction_generator(instructions):
        print(f"{instr}")
        counter +=1
        lookup = desert_map.get(lookup)[0 if instr == 'L' else 1]
        if lookup == end:
            break
    
    print(f"steps: {counter}")



        

        # if counter > 20_000_000: #failsafe to avoid endless loop
        #     break
