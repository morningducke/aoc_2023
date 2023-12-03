from functools import reduce
import operator
import re
from utils.parse import parse_lines

RED_CUBES = 12
GREEN_CUBES = 13
BLUE_CUBES = 14

cube_counts = {'red' : RED_CUBES, 'green' : GREEN_CUBES, 'blue' : BLUE_CUBES}

def is_game_possible(game: str) -> (int, int):
    game_info, sets = game.split(':')
    game_id = int(re.search(r"\d+", game_info).group(0))
    sets = sets.split(';')
    minimum_possible_cubes = {}
    for s in sets:
        for cube in s.split(','):   
            count, color = cube.strip().split(' ')
            count = int(count)
            minimum_possible_cubes[color] = max(minimum_possible_cubes[color], count) if color in minimum_possible_cubes else count
            if cube_counts[color] < count:
                game_id = 0
    return game_id, reduce(operator.mul, minimum_possible_cubes.values(), 1)

input_name = "input.txt"
sum_of_possible_ids = 0
sum_of_powers = 0
for line in parse_lines(input_name):
    id, power = is_game_possible(line)
    sum_of_possible_ids += id
    sum_of_powers += power

print(f"part 1, sum of possible ids: {sum_of_possible_ids}\npart 2, sum of minimum powers: {sum_of_powers}")   
