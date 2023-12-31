import re

num_regex = re.compile(r'[0-9]+')

with open('./input.txt') as data:
    lines = data.readlines()
    num_points = 0
    for line in lines:
        num_matches = 0
        winning_numbers = set(num_regex.findall(line[line.find(':'):line.find('|')]))
        actual_numbers = num_regex.findall(line[line.find('|'):])
        for actual_number in actual_numbers:
            if actual_number in winning_numbers:
                num_matches += 1
        if num_matches > 0:
            num_points += 2**(num_matches - 1)
    print(num_points)
        
