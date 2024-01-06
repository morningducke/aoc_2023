import re
from utils.linalg import transpose
from utils.parse import parse_matrix

def find_row_load(row: str) -> int:
    n = len(row)
    load = 0
    for m in re.finditer("([.O]+)((#+)|$)", row):
        # cur_load = 0
        for i in range(m.group(0).count("O")):
            # cur_load += n - m.start() - i
            load += n - m.start() - i
        # print(m.group(0), " ", cur_load)
    # print()
    return load
    
def find_north_load(matr: list[str]) -> int:
    total_load = 0
    for col in transpose(matr):
        total_load += find_row_load(col)
    return total_load

input_name = "input.txt"
matr = parse_matrix(input_name)
print(f"part 1, north load: {find_north_load(matr)}")