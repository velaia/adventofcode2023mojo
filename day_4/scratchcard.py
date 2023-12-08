import timeit

def main():
    sum_points = 0

    with open("input.txt", "r") as input:
        lines = input.readlines()
        for line in lines:
            winners = set(line[10:40].split())
            draws = set(line[42:].split())

            if (x := len(winners.intersection(draws))) > 0:
                sum_points += 2**(x - 1)
            
    print(f"{sum_points =}")
