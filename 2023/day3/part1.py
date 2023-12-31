import re

num_regex = re.compile(r'[0-9]+')

with open('./input.txt') as data:
    lines = data.readlines()
    # pad the matrix with '.'s to make processing easier
    lines.insert(0, '.' * len(lines[0]))
    lines.append('.' * len(lines[0]))
    part_num_sum = 0
    for line_num in range(1, len(lines) - 1):
        # pad the line with '.'s to make processing easier
        line = '.' + lines[line_num] + '.'
        prev_line = '.' + lines[line_num - 1] + '.'
        next_line = '.' + lines[line_num + 1] + '.'
        for num_match in num_regex.finditer(line):
            adjacent_chars = prev_line[num_match.start() - 1: num_match.end() + 1] + next_line[num_match.start() - 1:num_match.end() + 1] + line[num_match.start() - 1] + line[num_match.end()]
            if len(adjacent_chars.replace('.', '').strip()) > 0:
                part_num_sum += int(line[num_match.start():num_match.end()])
    print(part_num_sum)

                

