import re
from utils.parse import parse_matrix


def what_to_expand(matr: list[list[str]]) -> list[list[str]]:
    empty_line = "." * len(matr[0])
    rows_to_expand = [idx for idx, row in enumerate(matr) if row == empty_line]
    cols_to_expand = [idx for idx, col in enumerate(["".join(list(c)) for c in zip(*matr)]) if col == empty_line]
    return (rows_to_expand, cols_to_expand)

def find_galaxies(matr: list[list[str]]) -> list[tuple[int, int]]:
    galaxy_map = []
    for idx, row in enumerate(matr):
        for m in re.finditer("#", row):
            galaxy_map.append((idx, m.start()))
    return galaxy_map

def adjust_dist(x1: int, x2: int, lines_to_expand: list[int], adjust_coef : int = 1) -> int:
    adjusted_dist = 0
    for line_idx in lines_to_expand:
        if min(x1, x2) < line_idx < max(x1, x2):
            adjusted_dist += adjust_coef
    return adjusted_dist
        

def manhattan_adjusted(source: int, 
                       target: int, 
                       rows_to_expand: list[int], 
                       cols_to_expand: list[int],
                       adjust_coef : int = 1) -> int:
    
    y1, x1 = source
    y2, x2 = target
    adjusted_dist = adjust_dist(y1, y2, rows_to_expand, adjust_coef=adjust_coef) + adjust_dist(x1, x2, cols_to_expand, adjust_coef=adjust_coef)
    return abs(y2 - y1) + abs(x2 - x1) + adjusted_dist

def sum_min_paths(galaxy_map: list[tuple[int, int]], 
                  rows_to_expand: list[int], 
                  cols_to_expand: list[int],
                  adjust_coef : int = 1) -> int:
    
    path_sum = 0
    for i in range(len(galaxy_map)):
        for j in range(i + 1, len(galaxy_map)):
            path_sum += manhattan_adjusted(source=galaxy_map[i],
                                           target=galaxy_map[j],
                                           rows_to_expand=rows_to_expand,
                                           cols_to_expand=cols_to_expand,
                                           adjust_coef=adjust_coef)
    return path_sum
    

input_name = "input.txt"
matr = parse_matrix(input_name)
galaxy_map = find_galaxies(matr)
rows_to_expand, cols_to_expand = what_to_expand(matr)
print(f"part 1, sum of min paths {sum_min_paths(galaxy_map, rows_to_expand, cols_to_expand)}")
print(f"part 2, sum of min paths with older galaxies {sum_min_paths(galaxy_map, rows_to_expand, cols_to_expand, adjust_coef=1000000 - 1)}")
