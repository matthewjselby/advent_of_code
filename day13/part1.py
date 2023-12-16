import math

def find_reflection_point(lst):
    for l in range(len(lst) - 1):
        r = l + 1
        if lst[l] == lst[r]:
            lt = l
            rt = r
            while lt > 0 and rt < len(lst) - 1:
                lt -= 1
                rt += 1
                if lst[lt] != lst[rt]:
                    break
            if lst[lt] == lst[rt]:
                return l + 1
    return -1

with open('./input.txt') as data:
    lines = data.readlines()
    maps = []
    current_map = []
    for line in lines:
        if line == '\n':
            maps.append(current_map)
            current_map = []
        else:
            current_map.append(line.strip())
    maps.append(current_map)
    map_summary = 0
    for map in maps:
        rows = map
        cols = ['' for _ in range(len(rows[0]))]
        for row_idx, row in enumerate(rows):
            for col_idx in range(len(row)):
                cols[col_idx] = cols[col_idx] + row[col_idx]
        if (horizontal_reflection_point := find_reflection_point(rows)) != -1:
            map_summary += 100 * horizontal_reflection_point
        elif (vertical_reflection_point := find_reflection_point(cols)) != -1:
            map_summary += vertical_reflection_point
    print(map_summary)