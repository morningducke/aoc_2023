from enum import Enum
from utils.parse import parse_matrix
import sys

sys.setrecursionlimit(20000)

class Directions(Enum):
    NORTH = (-1, 0)
    SOUTH = (1, 0)
    WEST = (0, -1)
    EAST = (0, 1)

pipe_to_moves = {"|" : [Directions.NORTH.value, Directions.SOUTH.value],
                 "-" : [Directions.EAST.value, Directions.WEST.value],
                 "L" : [Directions.NORTH.value, Directions.EAST.value],
                 "J" : [Directions.NORTH.value, Directions.WEST.value],
                 "7" : [Directions.SOUTH.value, Directions.WEST.value],
                 "F" : [Directions.SOUTH.value, Directions.EAST.value],
                 "." : []
                 }

def check_valid_pos(pos: tuple[int, int], graph: list[list[str]]) -> bool:
    rows = len(graph)
    cols = len(graph[0])
    return pos[0] >= 0 and pos[0] < rows and pos[1] >= 0 and pos[1] < cols

def find_start_pipe(graph: list[list[str]]) -> tuple[int, int]:
    for i, row in enumerate(graph):
        for j, val in enumerate(row):
            if val == "S":
                return (i, j)
            
def sum_tuples(t1: tuple[int, ...], t2: tuple[int, ...]):
    return tuple([sum(elem) for elem in zip(t1, t2)])

def get_start_pipe(graph: list[list[str]], start_pos: tuple[int, int]) -> str:
    start_moves = []
    for d in Directions:
        neigh_pos = sum_tuples(start_pos, d.value)
        # print(f"neigh: {neigh_pos}")
        if not check_valid_pos(neigh_pos, graph):
            continue
        for move in pipe_to_moves[graph[neigh_pos[0]][neigh_pos[1]]]:
            # print(f"neigh's neigh: {sum_tuples(neigh_pos, move)}")
            if (sum_tuples(neigh_pos, move)) == start_pos:
                start_moves.append(d.value)

    for pipe, moves in pipe_to_moves.items():
        if set(moves) == set(start_moves):
            pipe_to_moves["S"] = moves # hack for convenience
            return pipe

def get_loop_length(graph: list[list[str]]):
    start_pos = start_pos = find_start_pipe(graph)
    print(f"start pos {start_pos}")
    start_pipe = get_start_pipe(graph, start_pos)
    print(f"start pipe: {start_pipe}")
    marked = set()
    def dfs(cur_pos: tuple[int, int]):
        if cur_pos in marked:
            return
        marked.add(cur_pos)
        for move in pipe_to_moves[graph[cur_pos[0]][cur_pos[1]]]:
            dfs(sum_tuples(cur_pos, move))
    dfs(start_pos)
    return len(marked)
    


input_name = "input.txt"    
graph = parse_matrix(input_name)
print("part 1, farthest loop point: ", get_loop_length(graph) // 2)


            
