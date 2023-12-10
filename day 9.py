from utils.parse import parse_lines

def extrapolate_value(nums: list[int]) -> tuple[int, int]:
    triangle = [nums]
    all_zeros = False
    while not all_zeros:
        all_zeros = True
        next_row = []
        for i in range(1, len(triangle[-1])):
            next_row.append(triangle[-1][i] - triangle[-1][i - 1])
            all_zeros = all_zeros and next_row[-1] == 0
        triangle.append(next_row)
    
    val_right = 0
    val_left = 0
    for i in range(len(triangle) - 2, -1, -1):
        val_left = triangle[i][0] - val_left
        val_right = val_right + triangle[i][-1]

    
    return val_left, val_right

def get_sum_extrapolated(input_name: str) -> tuple[int, int]:
    val_left = 0
    val_right = 0
    for line in parse_lines(input_name):
        vals = extrapolate_value([int(num) for num in line.split()])
        val_left += vals[0]
        val_right += vals[1]
    return val_left, val_right

input_name = "input.txt"

val_left, val_right = get_sum_extrapolated(input_name)
print(f"part 1, sum of right extrapolated values: {val_right}")
print(f"part 2, sum of left extrapolated values: {val_left}")
    