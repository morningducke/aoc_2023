from utils.parse import parse_matrices

def hamming_dist(lhs: str, rhs: str) -> int:
    return sum(l != r for l,r in zip(lhs, rhs))

def find_symmetry_axis(matr: list[str]) -> int:
    for i in range(0, len(matr) - 1):
        is_axis = True
        for k in range(min(i + 1, len(matr) - i - 1)):
            if matr[i - k] != matr[i + k + 1]:
                is_axis = False
                break
        if is_axis:
            return i + 1
    return 0

def find_smidged_axis(matr: list[str]) -> int:
    for i in range(0, len(matr) - 1):
        total_hamming = 0
        for k in range(min(i + 1, len(matr) - i - 1)):
            total_hamming += hamming_dist(matr[i - k], matr[i + k + 1])
            if total_hamming > 1:
                break
        if total_hamming == 1:
            return i + 1
    return 0

def transpose(matr: list[str]) -> list[str]:
    return ["".join(row) for row in zip(*matr)]

input_name = "input.txt"
part_1 = 0
part_2 = 0
for matr in parse_matrices(input_name):
    row_axis = find_symmetry_axis(matr)
    if row_axis:
        part_1 += 100 * row_axis
    else:
        part_1 += find_symmetry_axis(transpose(matr))
        
    row_axis_smidged = find_smidged_axis(matr)
    if row_axis_smidged:
        part_2 += 100 * row_axis_smidged
    else:
        part_2 += find_smidged_axis(transpose(matr))

print(f"part 1: {part_1}")
print(f"part 2: {part_2}")

