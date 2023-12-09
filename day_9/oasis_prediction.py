import numpy as np

dev = "input_sample.txt"
prod = "input.txt"
system = prod

timelines = []

with open(system, "r") as input:
    while timeline := input.readline():
        timelines.append([int(elem) for elem in timeline.split()])

timelines = np.array(timelines)

extrap_sum = 0
for timeline in timelines:
    extrap = 0
    for i in range(1, len(timeline)):
        diffs = np.diff(timeline, n=i)
        extrap += diffs[-1]
        if np.all(diffs == 0):
            extrap_sum += timeline[-1] + extrap
            break
print(extrap_sum)