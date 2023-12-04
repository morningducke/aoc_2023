from utils.parse import parse_lines
from collections import defaultdict

def extract_nums(nums: str):
    return nums.strip().split()  

def count_matches(card_string: str):
    _, numbers = card_string.split(':')
    winning_nums, card_nums = numbers.split('|')
    winning_nums = set(extract_nums(winning_nums))
    card_nums = set(extract_nums(card_nums))
    # assumes no repeated numbers
    return len(winning_nums.intersection(card_nums))

def count_card_value(matches):
    return 2 ** (matches - 1) if matches >= 1 else 0

input_name = "input.txt"
total_cards_value = 0 # part 1
cards_amount = defaultdict(int) # part 2
for card_id, line in enumerate(parse_lines(input_name)): 
    cards_amount[card_id] += 1
    matches = count_matches(line)
    total_cards_value += count_card_value(matches)
    for next_card in range(card_id + 1, card_id + 1 + matches):
        cards_amount[next_card] += cards_amount[card_id]

print(f"part 1, total cards value: {total_cards_value}")
print(f"part 2, total cards : {sum(cards_amount.values())}")

