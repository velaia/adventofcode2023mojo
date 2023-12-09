import numpy as np

dev = "input_sample.txt"
prod = "input.txt"
system = prod


def main():
    timelines = []
    with open(system, "r") as input:
        while timeline := input.readline():
            timelines.append([int(elem) for elem in timeline.split()])


    timelines = np.array(timelines)
    all_extrapolated = 0

    for timeline in timelines:
        backwards_extrap = []
        for i in range(1, len(timeline)):
            diffs = np.diff(timeline, n=i)
            backwards_extrap.append(diffs[0])
            if np.all(diffs == 0):
                break
        backwards_extrap.insert(0, timeline[0])

        previous = 0
        sum_prev = 0
        for i in range(1, len(backwards_extrap)):
            previous = backwards_extrap[-i -1] - previous
            sum_prev += previous
        
        all_extrapolated += previous

    # print(all_extrapolated)
