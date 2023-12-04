from utils.parse import parse_matrix
import re

RECTANGLE_HEIGHT = 3

def form_query(row: int, first_col: int, last_col: int):
    """Forms a query rectangle represented by three values: first row, first col and last col"""
    return [row - 1, first_col - 1, last_col + 1]

def bound_rectangle(matrix: list[str], query: list[int]):
    first_row, first_col, last_col = query
    last_row = first_row + RECTANGLE_HEIGHT
    first_row = max(first_row, 0)
    first_col = max(first_col, 0)
    last_col = min(last_col, len(matrix[0]))
    last_row = min(last_row, len(matrix))
    return first_row, first_col, last_row, last_col

def is_symbol_adjacent(matrix: list[str], query: list[int]):
    """Checks if any symbols are in the rectangle formed by a number"""
    first_row, first_col, last_row, last_col = bound_rectangle(matrix, query)
    for row in range(first_row, last_row):
        for col in range(first_col, last_col):
            char = matrix[row][col]
            if char != '.' and not char.isdigit():
                return True
    return False

def sum_part_numbers(matrix: list[str]):
    total_sum = 0
    for idx, row in enumerate(matrix):
        for number in re.finditer(r"\d+", row):
            # print(f"row: {idx}, cols: {number.group(0)} : {number.start(0)}, {number.end(0) - 1}, is_adj: {is_symbol_adjacent(matrix, form_rectangle(idx, number.start(0), number.end(0)))}")
            # print(f"query: {form_rectangle(idx, number.start(0), number.end(0))}")
            total_sum += int(number.group(0)) if is_symbol_adjacent(matrix, form_query(idx, number.start(0), number.end(0))) else 0 
    return total_sum

def add_gear_neighbor(matrix: list[str],  query: list[int], number: int, candidate_gear: dict):
    first_row, first_col, last_row, last_col = bound_rectangle(matrix, query)
    for row in range(first_row, last_row):
        for col in range(first_col, last_col):
            char = matrix[row][col]
            if char == '*':
                if (row, col) in candidate_gear:
                    candidate_gear[(row, col)].append(number)
                else:
                    candidate_gear[(row, col)] = [number]
    

# can find gears while summing part numbers but for the sake of task separation it's in its own function
def find_gears(matrix: list[str]):
    candidates = {}
    for idx, row in enumerate(matrix):
        for number in re.finditer(r"\d+", row):
            add_gear_neighbor(matrix, form_query(idx, number.start(0), number.end(0)), int(number.group(0)), candidates)            
    return candidates

def sum_gear_ratios(matrix: list[str]):
    candidates = find_gears(matrix)
    total_gear_ratios = 0
    for numbers in candidates.values():
        total_gear_ratios += numbers[0] * numbers[1] if len(numbers) == 2 else 0
    return total_gear_ratios

input_name = "input.txt"
matrix = parse_matrix(input_name)
print(f"part 1, sum of part numbers: {sum_part_numbers(matrix)}")
print(f"part 2, sum of gear ratios: {sum_gear_ratios(matrix)}")


