from enum import Enum
import re
from utils.linalg import row_reverse, transpose
from utils.parse import parse_matrix

class Directions(Enum):
    NORTH = 0
    WEST = 1
    SOUTH = 2
    EAST = 3 
    
CYCLE_PATH = [Directions.NORTH, Directions.WEST, Directions.SOUTH, Directions.EAST]
TOTAL_CYCLES = 1000000000

def find_row_load(row: str) -> int:
    n = len(row)
    load = 0
    for m in re.finditer("#*([.O])+((#+)|$)", row):
        # cur_load = 0
        for i, char in enumerate(m.group(0)):
            if char == 'O':
                # cur_load += n - m.start() - i
                load += n - m.start() - i
        #  print(m.group(0), " ", cur_load)
    # print()
    return load

def find_north_load(matr: list[str]) -> int:
    total_load = 0
    for col in transpose(matr):
        total_load += find_row_load(col)
    return total_load
    
def simulate_row_rockfall(row: str) -> str:
    """Simulate west-bound rockfall (rocks to the left)"""
    separated_rocks = []
    for m in re.finditer("#*([.O])+((#+)|$)", row):
        matched_str = m.group(0)
        new_row = []
        if matched_str.startswith("#"):
            # kinda unreadable but we find the first non #
            new_row.append(matched_str[:re.search("[^#]", matched_str).start()])
            
        rocks = matched_str.count("O")
        spaces = matched_str.count(".")
        new_row.append("O" * rocks + "." * spaces)

        if matched_str.endswith("#"):
            # find the last non #
            new_row.append(matched_str[max(matched_str.rfind("O"), matched_str.rfind(".")) + 1:])
        
        separated_rocks.append("".join(new_row))
    return "".join(separated_rocks)
        

def simulate_rockfall(matr: list[str]) -> list[str]:
    simulated_matr = []
    for row in matr:
        simulated_matr.append(simulate_row_rockfall(row))
    
    return simulated_matr

def tilt(matr: list[str], direction: Directions) -> list[str]:
    tilted_matr = None
    match direction:
        case Directions.NORTH:
            tilted_matr = transpose(simulate_rockfall(transpose(matr)))
        case Directions.WEST:
            tilted_matr = simulate_rockfall(matr)
        case Directions.SOUTH:
            tilted_matr = transpose(row_reverse(simulate_rockfall(row_reverse(transpose(matr)))))
        case Directions.EAST:
            tilted_matr = row_reverse(simulate_rockfall(row_reverse(matr)))
        case _:
            raise ValueError("no such direction")
    return tilted_matr
    

def tilt_cycle(matr: list[str]) -> list[str]:
    tilted_matr = matr
    for direction in CYCLE_PATH:
        tilted_matr = tilt(tilted_matr, direction)
    return tilted_matr
    
def find_loop(matr: list[str]) -> list[str]:
    cycle_num = 0
    tilted_matr = matr
    states = {}
    # could be done more effieciently by hashing rock positions
    while "".join(tilted_matr) not in states:
        states["".join(tilted_matr)] = cycle_num
        tilted_matr = tilt_cycle(tilted_matr)
        cycle_num += 1
        
    cycle_length = cycle_num - states["".join(tilted_matr)]
    position_after_cycles = (TOTAL_CYCLES - cycle_num + 1) % cycle_length
    for _ in range(position_after_cycles - 1):
        tilted_matr = tilt_cycle(tilted_matr)
        
    return cycle_num, cycle_length, position_after_cycles, tilted_matr
        
    
input_name = "input.txt"
matr = parse_matrix(input_name)
print(f"part 1, north load: {find_north_load(tilt(matr, Directions.NORTH))}")
print(f"part 2, north load after cycles: {find_north_load(find_loop(matr)[-1])}")

