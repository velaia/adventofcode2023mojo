import numpy as np
import itertools
import multiprocessing

def main():
    input = [line for line in open("input.txt").readlines() if len(line) > 0]
    width, height = len(input[0]), len(input)

    def create_map(input) -> np.array:
        game_map = np.zeros((height, width), dtype='bool')
        for idx, line in enumerate(input):
            game_map[idx] = np.array([char == "#" for char in line], dtype='bool')
        return game_map

    game_map = create_map(input)
    empty_rows = np.argwhere(np.invert(np.apply_along_axis(np.any, axis=1, arr=game_map))).flatten()
    empty_cols = np.argwhere(np.invert(np.apply_along_axis(np.any, axis=0, arr=game_map))).flatten()

    def get_dist(edge: tuple) -> int:
        return np.abs(edge[0][0] - edge[1][0]) + np.abs(edge[0][1] - edge[1][1])

    # updated + part 1 + 2
    multipliers = (1, 1_000_000 - 1)
    for j, expansion_multiplier in enumerate(multipliers):
        G = []
        for node in np.argwhere(game_map):
            G.append((node[0] + np.searchsorted(empty_rows, node[0]) * expansion_multiplier,
                      node[1] + np.searchsorted(empty_cols, node[1]) * expansion_multiplier))

        all_distances = 0
        pool = multiprocessing.Pool()
        pool.map(lambda x: x[0][0] + x[0][1], tuple(itertools.combinations(G, 2)))
        # for i in itertools.combinations(G, 2):
        #      all_distances += abs(i[0][0] - i[1][0]) + abs(i[0][1] - i[1][1])
        print(f"part {j+1}: {all_distances}")

def get_dist(i):
    return abs(i[0][0] - i[1][0]) + abs(i[0][1] - i[1][1])


if __name__ == "__main__":
    main()