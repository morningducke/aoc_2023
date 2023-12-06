from math import ceil, floor

"""explanation: S = v * t, where t = time left when button released, let tau = time the button was held for whcih equals v
   then T = t + tau - total time in the race
   S = v * t = tau * t = tau*(T - tau) = tau*T - tau^2
   we have a downward parabola with a maximum at tau = T/2
   therefore we just have to find the part of parabola which lies above y = S_r, where S_r is the record distance
"""

def parse_races(file_name: str) -> list[tuple[int, int]]:
    races = []
    with open(file_name, "r") as f:
        times = f.readline().split(':')[1].split()
        dists = f.readline().split(':')[1].split()
    return [(int(time), int(dist)) for time, dist in zip(times, dists)]

def calc_ways(T: int, S_r: int) -> int:
    d = T**2 - 4*S_r
    if d < 0:
        return 0
    elif d == 0:
        # accounting for a case when intersects in one point but not on an integer value
        return T % 2 == 0

    d_sqrt = (T**2 - 4*S_r)**(1/2)
    return ceil((T + d_sqrt) / 2 - 1) - floor((T - d_sqrt) / 2 + 1) + 1

    
def calc_races(races: list) -> int:
    ways = 1
    for race in races:
        print(f"race: {race}, ways = {calc_ways(race[0], race[1])}")
        ways *= calc_ways(race[0], race[1])
    return ways

def parse_race_part2(file_name: str) -> tuple[int ,int]:
    with open(file_name, "r") as f:
        time = int("".join(f.readline().split(':')[1].split()))
        dist = int("".join(f.readline().split(':')[1].split()))
        return (time, dist)

input_name = "input.txt"
races = parse_races(input_name)
print(f"part 1, ways multplied = {calc_races(races)}")
print(f"part 2, ways multplied = {calc_races([parse_race_part2(input_name)])}")

    