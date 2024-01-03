import re
from functools import cache
from utils.parse import parse_lines

# brute force

# def is_valid(record: list[str], groups: list[int]) -> bool:
#     record_string = "".join(record).strip(".")
#     return [len(m) for m in re.findall(r"#+", record_string)] == groups
    


# def count_arrangements(record: list[str], groups: list[int], cur_idx : int = 0) -> int:
#     if cur_idx == len(record):
#         return 1 if is_valid(record, groups) else 0
#     ans = 0
#     # print(record, groups)
#     if record[cur_idx] == "?":
#         record[cur_idx] = "#"
#         ans += count_arrangements(record, groups, cur_idx=cur_idx + 1) 
#         record[cur_idx] = "."
#         ans += count_arrangements(record, groups, cur_idx=cur_idx + 1)
#         record[cur_idx] = "?"
#     else:
#         ans = count_arrangements(record, groups, cur_idx=cur_idx + 1)

#     return ans


# credit to https://www.reddit.com/r/adventofcode/comments/18ge41g/comment/kd0oj1t/?utm_source=share&utm_medium=web2x&context=3
@cache
def count_arrangements(record: str, groups: tuple[int, ...]) -> int:
    record = record.lstrip(".")

    if record == "":
        return groups == ()
    if groups == ():
        return "#" not in record
    
    if record[0] == '#':
        if len(record) < groups[0] or '.' in record[:groups[0]]:
            return 0 
        elif len(record) == groups[0]:
            return len(groups) == 1
        elif record[groups[0]] == '#':
            return 0 
        else:
            return count_arrangements(record[groups[0]+1:], groups[1:])

    return count_arrangements('#'+record[1:], groups) + count_arrangements(record[1:], groups)

input_name = "input.txt"
sum_of_arrangements = 0
sum_of_arrangements_unfolded = 0

for num, line in enumerate(parse_lines(input_name)):
    record, groups = line.split(" ")
    groups = tuple(int(group) for group in groups.split(","))
    sum_of_arrangements += count_arrangements(record, groups)
    sum_of_arrangements_unfolded += count_arrangements("?".join([record] * 5), groups * 5)

print("part 1: ", sum_of_arrangements)
print("part 2: ", sum_of_arrangements_unfolded)