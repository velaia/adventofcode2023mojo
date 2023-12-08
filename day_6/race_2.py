from math import sqrt, ceil, floor


dev = "input_sample_2.txt"
prod = "input_2.txt"
active = prod

with open(active, "r") as input:
    time = [int(val) for val in input.readline().split()[1:]]
    distance = [int(val) for val in input.readline().split()[1:]]
    overall_ways_of_winning_product = 1

    time_dist = zip(time, distance)

    for i, (time, dist) in enumerate(time_dist):
        print(f"race {i + 1}: {time =}, {dist =}")
        x_1 = floor((-time + sqrt(time**2 - 4*(-1)*(-dist)))/2)
        x_2 = ceil((-time - sqrt(time**2 - 4*(-1)*(-dist)))/2)

        print(f"race {i+1}: bounds {x_2} - {x_1}; {x_1 - x_2 + 1} ways of winning")
        overall_ways_of_winning_product *= (x_1 - x_2 + 1)
    
    print(f"result: {overall_ways_of_winning_product}")