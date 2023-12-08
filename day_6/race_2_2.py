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
        lower_bound, upper_bound = 0, time
        for x in range(0, time):
            if (time - x) * x > dist:
                lower_bound = x
                break
        
        for x in range(time, 0, -1):
            if (time - x) * x > dist:
                upper_bound = x
                break

        print(f"race {i+1}: bounds {lower_bound} - {upper_bound}; {upper_bound - lower_bound + 1} ways of winning")
        overall_ways_of_winning_product *= (upper_bound - lower_bound + 1)
    
    print(f"result: {overall_ways_of_winning_product}")