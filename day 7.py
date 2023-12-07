from functools import cmp_to_key
from utils.parse import parse_lines
from collections import Counter
import numpy as np

class Hand:
    def __init__(self, hand: str, value: int):
        self.hand = hand
        self.value = value
    
    def __str__(self) -> str:
        return str((self.hand, self.value))
    
    def __repr__(self) -> str:
        return self.__str__()

def parse_hand(hand: str) -> Hand:
    hand, val = hand.split()
    return Hand(hand, int(val))
    
def is_five_of_a_kind(card_counter: Counter) -> bool:
    return len(card_counter) == 1

def is_four_of_a_kind(card_counter: Counter) -> bool:
    return any(count == 4 for count in card_counter.values())

def is_full_house(card_counter: Counter) -> bool:
    sorted_count = card_counter.most_common()
    return sorted_count[0][1] == 3 and sorted_count[1][1] == 2

def is_three_of_a_kind(card_counter: Counter) -> bool:
    return card_counter.most_common()[0][1] == 3 and not is_full_house(card_counter)

def is_two_pair(card_counter: Counter) -> bool:
    sorted_count = card_counter.most_common()
    return sorted_count[0][1] == 2 and sorted_count[1][1] == 2

def is_pair(card_counter: Counter) -> bool:
    return card_counter.most_common()[0][1] == 2 and not is_two_pair(card_counter)

def is_high_card(card_counter: Counter) -> bool:
    return len(card_counter) == 5

def get_hand_strength(hand: Hand) -> int:
    card_counter = Counter(hand.hand)

    if is_five_of_a_kind(card_counter):
        return 7
    if is_four_of_a_kind(card_counter):
        return 6
    if is_full_house(card_counter):
        return 5
    if is_three_of_a_kind(card_counter):
        return 4
    if is_two_pair(card_counter):
        return 3
    if is_pair(card_counter):
        return 2
    if is_high_card(card_counter):
        return 1
    
    return 0

def get_hand_strength_part2(hand: Hand) -> int:
    card_counter = Counter(hand.hand)
    # solves 5 jokers case
    if is_five_of_a_kind(card_counter):
        return 7
    
    non_jokers = [card for card in card_counter.keys() if card != 'J']
    max_score = 0
    for card in non_jokers:
        score = get_hand_strength(Hand(hand.hand.replace("J", card), hand.value))
        max_score = max(max_score, score)
    
    return max_score

def get_card_value_map(part2=False) -> dict[str, int]:
    card_value_map = dict(zip([num for num in "23456789"], range(2, 10)))
    if part2:
        card_value_map.update({"T" : 10, "J" : 0, "Q": 12, "K": 13, "A": 14})
    else:
        card_value_map.update({"T" : 10, "J" : 11, "Q": 12, "K": 13, "A": 14})
    return card_value_map

def card_cmp(lhs: Hand, rhs: Hand) -> int:
    card_value_map = get_card_value_map()
    lhs_mapped = [card_value_map[c] for c in lhs.hand]
    rhs_mapped = [card_value_map[c] for c in rhs.hand]
    if lhs_mapped > rhs_mapped:
        return 1
    if lhs_mapped == rhs_mapped:
        return 0
    return -1

def card_cmp_part2(lhs: Hand, rhs: Hand) -> int:
    card_value_map = get_card_value_map(part2=True)
    lhs_mapped = [card_value_map[c] for c in lhs.hand]
    rhs_mapped = [card_value_map[c] for c in rhs.hand]
    if lhs_mapped > rhs_mapped:
        return 1
    if lhs_mapped == rhs_mapped:
        return 0
    return -1

def sort_hands(hands: list[Hand], part2=False) -> list[Hand]:
    sorted_hands = sorted(hands, key=cmp_to_key(card_cmp_part2 if part2 else card_cmp))
    return sorted(sorted_hands, key=get_hand_strength_part2 if part2 else get_hand_strength)


def get_total_winnings(sorted_hands: list[Hand]) -> int:
    """as dot product for fun"""
    n = len(sorted_hands)
    placement_vec = np.array(range(1, n + 1))
    values_vec = np.array([hand.value for hand in sorted_hands])
    return placement_vec.dot(values_vec)

input_name = "input.txt"
hands = [parse_hand(line) for line in parse_lines(input_name)]
print(f"part 1, total winnings: {get_total_winnings(sort_hands(hands))}")
print(f"part 2, total winnings: {get_total_winnings(sort_hands(hands, part2=True))}")

