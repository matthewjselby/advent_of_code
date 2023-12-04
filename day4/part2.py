import re

num_regex = re.compile(r'[0-9]+')

with open('./input.txt') as data:
    lines = data.readlines()
    card_map = dict([(line_num, 1) for line_num in range(1, len(lines) + 1)])
    for line_num, line in enumerate(lines):
        num_matches = 0
        winning_numbers = set(num_regex.findall(line[line.find(':'):line.find('|')]))
        actual_numbers = num_regex.findall(line[line.find('|'):])
        for actual_number in actual_numbers:
            if actual_number in winning_numbers:
                num_matches += 1
        if num_matches > 0:
            for match_num in range(1, num_matches + 1):
                card_map[line_num + 1 + match_num] += (1 * card_map[line_num + 1])
    total_cards = sum(card_map.values())
    print(total_cards)