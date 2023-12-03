from utils.parse import parse_lines

NUMBER_NAMES = {"one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9}

def find_calibration_value(text: str) -> int:
    first_pos = -1
    first_number = -1
    last_pos = -1
    last_number = -1
    for number in list(NUMBER_NAMES.keys()) + list(range(1, 10)):
        pos_l = text.find(str(number))
        pos_r = text.rfind(str(number))
        if pos_l != -1 and (first_pos == -1 or pos_l < first_pos):
            first_pos = pos_l
            first_number = number if isinstance(number, int) else NUMBER_NAMES[number]
        if pos_r != -1 and (pos_r > last_pos):
            last_pos = pos_r
            last_number = number if isinstance(number, int) else NUMBER_NAMES[number]
    return first_number * 10 + last_number

input_name = "input.txt"
sum_of_calibration_vals = 0
for line in parse_lines(input_name):
    sum_of_calibration_vals += find_calibration_value(line)
print(f"part 2, sum of calibration values: {sum_of_calibration_vals}")        
    
    
