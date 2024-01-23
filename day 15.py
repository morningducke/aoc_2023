from collections import defaultdict
from utils.parse import parse_lines

def hash(s: str) -> int:
    res = 0
    for code in s.encode("ascii"):
        res += code
        res *= 17
        res %= 256
    return res

def get_focusing_power_sum(boxes: defaultdict[int, dict[str, int]]) -> int:
    focusing_power_sum = 0
    for box, lenses in boxes.items():
        for pos, focal_length in enumerate(lenses.values()):
            focusing_power_sum += (box + 1) * (pos + 1) * focal_length
    return focusing_power_sum
        
input = "input.txt"
data = next(parse_lines(input))
hash_sum = 0
# could be a list of length 256 instead but this generalizes better in case mod > 256
boxes = defaultdict(dict)

# part 1
for s in data.split(","):
    hash_sum += hash(s)
    
# part 2
for s in data.split(","):
    if s[-1] == "-":
        label = s[:-1]
        hash_value = hash(label)
        if hash_value in boxes and label in boxes[hash_value]:
            boxes[hash_value].pop(label)
    else:
        label, focal_length = s.split("=")        
        hash_value = hash(label)
        boxes[hash_value][label] = int(focal_length)

print(f"part 1, sum of hashes: {hash_sum}")
print(f"part 2, sum of focusing power: {get_focusing_power_sum(boxes)}")