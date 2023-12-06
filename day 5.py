import re

def map_to_nums(nums: str, cur_map: dict):
    dest_start, source_start, range_len = [int(n) for n in nums.split()]
    for k in cur_map.keys():
        if source_start <= k <= source_start + range_len - 1:
            cur_map[k] = dest_start + (k - source_start)

def parse_almanac_part_1(file_name: str):
    map_sequence = {}
    with open(file_name, "r") as almanac:
        seeds = almanac.readline()
        for number in re.finditer(r"\d+", seeds):
            map_sequence[int(number.group(0))] = int(number.group(0))

        for line in almanac:
            if "map" in line:
                while (nums := almanac.readline()) != "\n" and nums != "":
                    map_to_nums(nums, map_sequence)
                # shift values into keys for the next iteration
                new_map = {}
                for v in map_sequence.values():
                    new_map[v] = v
                map_sequence = new_map

    return map_sequence

class CustomRange:
    """A 1D range [start, end] that can perform intersection operation on another range"""

    def __init__(self, start: int, end: int | None = None, length: int | None = None) -> None:
        if end is None and length is None:
            raise ValueError("Either end or length should be passed")
        
        self.start = start
        self.end = start + length - 1 if length else end

    def intersection(self, range):
        intersection_start = max(self.start, range.start)
        intersection_end = min(self.end, range.end)
        return CustomRange(start=intersection_start, end=intersection_end) if intersection_start <= intersection_end else None

    def length(self):
        return self.end - self.start + 1
    
    def is_valid(self):
        return self.end >= self.start

    def __str__(self) -> str:
        return f"({self.start}, {self.end})"
    
    def __repr__(self):
        return str(self)
    
def parse_seed_ranges(seeds: str) -> list:
    seed_nums = [int(s) for s in seeds.split()]
    seed_ranges = []
    for i in range(0, len(seed_nums), 2):
        seed_ranges.append(CustomRange(start=seed_nums[i], length=seed_nums[i + 1]))
    return seed_ranges

def map_ranges(nums: str, ranges: list) -> list:
    dest_start, source_start, range_len = [int(n) for n in nums.split()]
    dest_r = CustomRange(start=dest_start, length=range_len)
    source_r = CustomRange(start=source_start, length=range_len)
    new_ranges = []
    leftovers = []
    while ranges:
        r = ranges.pop()
        # split the range into the intersecting part, and the parts left and right of it
        inter_r = source_r.intersection(r)
        before_r = CustomRange(start=r.start, end=min(r.end, source_r.start - 1))
        after_r = CustomRange(start=max(source_r.end + 1, r.start), end=r.end)
        if inter_r:
            dest_offset = inter_r.start - source_r.start
            new_ranges.append(CustomRange(start=dest_r.start + dest_offset, length=inter_r.length()))
        if before_r.is_valid():
            leftovers.append(before_r)
        if after_r.is_valid():
            leftovers.append(after_r)
        
    return new_ranges, leftovers    
        

def parse_almanac_part_2(file_name: str):
    ranges = []
    with open(file_name, "r") as almanac:
        ranges = parse_seed_ranges(almanac.readline().split(':')[1])
        for line in almanac:
            if "map" in line:
                next_ranges = []
                while (nums := almanac.readline()) != "\n" and nums != "":
                    mapped = map_ranges(nums, ranges)
                    next_ranges += mapped[0] # ranges that got mapped
                    ranges = mapped[1] # leftover ranges that didnt get mapped yet
                ranges += next_ranges
    return ranges
                    
input_name = "input.txt"
locaton_map = parse_almanac_part_1(input_name)
print(f"part 1, lowest location: {min(list(locaton_map.keys()))}")
locaton_map = parse_almanac_part_2(input_name)
print(f"part 2, lowest location: {min([loc_r.start for loc_r in locaton_map])}")