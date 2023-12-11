import numpy as np
import networkx as nx


input = [line for line in open("input.txt").readlines() if len(line) > 0]
width, height = len(input[0]), len(input)

def create_map(input) -> np.array:
    game_map = np.zeros((height, width), dtype='bool')
    for idx, line in enumerate(input):
        game_map[idx] = np.array([char == "#" for char in line], dtype='bool')
    return game_map

def expand_space(game_map: np.array) -> np.array:
    empty_rows = np.argwhere(np.invert(np.apply_along_axis(np.any, axis=1, arr=game_map))).flatten()
    empty_cols = np.argwhere(np.invert(np.apply_along_axis(np.any, axis=0, arr=game_map))).flatten()
    game_map = np.insert(game_map, empty_rows, False, axis=0)
    game_map = np.insert(game_map, empty_cols, False, axis=1)
    return game_map

def get_dist(edge: tuple) -> int:
    return np.abs(edge[0][0] - edge[1][0]) + np.abs(edge[0][1] - edge[1][1])

game_map = create_map(input)
expanded_map = expand_space(game_map)

G = nx.Graph()
for node in np.argwhere(expanded_map):
    G.add_node((node[0], node[1]))

CG: nx.Graph = nx.complete_graph(G.nodes)
i = sum([get_dist(edge) for edge in CG.edges])
print(i)


