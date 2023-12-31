import re

digit_map = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

with open('./input.txt') as input:
    lines = input.readlines()
    total = 0
    for line in lines:
        digit_regex = re.compile('(?=([1-9]|one|two|three|four|five|six|seven|eight|nine))')
        matches = digit_regex.findall(line)
        first_digit = digit_map[matches[0]]
        second_digit = digit_map[matches[-1]]
        total += (first_digit * 10) + second_digit
    print(total)