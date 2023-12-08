dev = "input_sample.txt"
prod = "input.txt"
system = prod

rank = reversed("A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2".replace(',', '').split())
rank = [i for i in rank]


def value(entry: str) -> list:
    """returns the value of a hand used for sorting
    """
    counts = []
    hand = entry[0]

    # house, full house, pair, ... for primary sorting
    for character in iter(set(hand)):
        counts.append(hand.count(character))
    counts = sorted(counts, reverse=True)

    # add the cards for additional sorting / scoring
    for i in range(len(hand)):
        counts.append(rank.index(hand[i]))
    return counts

with open(system, "r") as input:
    entries = []
    while line := input.readline():
        entry = line.split()
        entry = (entry[0], int(entry[1]))
        entries.append(entry)
    sorted_entries = sorted(entries, key=value)
    
    bid_product = 0
    for i, entry in enumerate(sorted_entries):
        bid_product += entry[1] * (i + 1)

    print(f"{bid_product =}")
