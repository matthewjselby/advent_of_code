import re

num_regex = re.compile(r'[0-9]+')
symbol_map = {}

def get_adjacent_indices(line, start, end):
    adjacent_indices = []
    for i in range(line - 1, line + 2):
        for j in range(start - 1, end + 1):
            if not (i == line and j < end and j >= start):
                adjacent_indices.append((i, j))
    return adjacent_indices

with open('./input.txt') as data:
    lines = data.readlines()
    # pad the matrix with '.'s to make processing easier
    lines.insert(0, '.' * len(lines[0]))
    lines.append('.' * len(lines[0]))
    for line_index in range(len(lines)):
        lines[line_index] = '.' + lines[line_index] + '.'
    part_num_sum = 0
    for line_num in range(1, len(lines) - 1):
        for num_match in num_regex.finditer(line):
            adjacent_indices = get_adjacent_indices(line_num, num_match.start(), num_match.end())
            for adjacent_index in adjacent_indices:
                if lines[adjacent_index[0]][adjacent_index[1]] == '*':
                    if adjacent_index in symbol_map:
                        symbol_map[adjacent_index].append(int(lines[line_num][num_match.start():num_match.end()]))
                    else:
                        symbol_map[adjacent_index] = [int(lines[line_num][num_match.start():num_match.end()])]
    for value in symbol_map.values():
        if len(value) == 2:
            part_num_sum += value[0] * value[1]
    print(part_num_sum)
                    
            
                
    
        