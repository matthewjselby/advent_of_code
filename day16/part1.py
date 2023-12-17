import sys
sys.setrecursionlimit(5000)

with open('./input.txt') as data:
    map = [list(line.strip()) for line in data.readlines()]
    energized_map = [[set() for _ in range(len(line))] for line in map]

    def traverse_map(pos, dir):
        global map
        global energized_map

        row = pos[0]
        col = pos[1]

        if  row < 0 or row >= len(map) or col < 0 or col >= len(map[0]) or dir in energized_map[row][col]:
            return

        energized_map[row][col].add(dir)

        if dir == 'n':
            if map[row][col] in '.|':
                traverse_map((row - 1, col), 'n')
            elif map[row][col] == '/':
                traverse_map((row, col + 1), 'e')
            elif map[row][col] == '\\':
                traverse_map((row, col - 1), 'w')
            elif map[row][col] == '-':
                traverse_map((row, col + 1), 'e')
                traverse_map((row, col - 1), 'w')
        elif dir == 's':
            if map[row][col] in '.|':
                traverse_map((row + 1, col), 's')
            elif map[row][col] == '/':
                traverse_map((row, col - 1), 'w')
            elif map[row][col] == '\\':
                traverse_map((row, col + 1), 'e')
            elif map[row][col] == '-':
                traverse_map((row, col + 1), 'e')
                traverse_map((row, col - 1), 'w')
        elif dir == 'e':
            if map[row][col] in '.-':
                traverse_map((row, col + 1), 'e')
            elif map[row][col] == '/':
                traverse_map((row - 1, col), 'n')
            elif map[row][col] == '\\':
                traverse_map((row + 1, col), 's')
            elif map[row][col] == '|':
                traverse_map((row - 1, col), 'n')
                traverse_map((row + 1, col), 's')
        elif dir == 'w':
            if map[row][col] in '.-':
                traverse_map((row, col - 1), 'w')
            elif map[row][col] == '/':
                traverse_map((row + 1, col), 's')
            elif map[row][col] == '\\':
                traverse_map((row - 1, col), 'n')
            elif map[row][col] == '|':
                traverse_map((row - 1, col), 'n')
                traverse_map((row + 1, col), 's')
        
    entry_options = [((0, 0), ['e', 's']), ((0, len(energized_map[0]) - 1), ['s', 'w']), ((len(energized_map) - 1, 0), ['e', 'n']), ((len(energized_map) - 1, len(energized_map[0]) - 1), ['n', 'w'])]
    
    max_num_energized_tiles = 0

    def count_energized_tiles(energized_map):
        num_energized_tiles = 0
        for row in energized_map:
            for col in row:
                if len(col) > 0:
                    num_energized_tiles += 1
        return num_energized_tiles

    for row in range(len(map)):
        energized_map = [[set() for _ in range(len(line))] for line in map]
        traverse_map((row, 0) , 'e')
        num_energized_tiles = count_energized_tiles(energized_map)
        if num_energized_tiles > max_num_energized_tiles:
            max_num_energized_tiles = num_energized_tiles
        energized_map = [[set() for _ in range(len(line))] for line in map]
        traverse_map((row, len(map[row]) - 1) , 'w')
        num_energized_tiles = count_energized_tiles(energized_map)
        if num_energized_tiles > max_num_energized_tiles:
            max_num_energized_tiles = num_energized_tiles

    for col in range(len(map[0])):
        energized_map = [[set() for _ in range(len(line))] for line in map]
        traverse_map((0, col) , 's')
        num_energized_tiles = count_energized_tiles(energized_map)
        if num_energized_tiles > max_num_energized_tiles:
            max_num_energized_tiles = num_energized_tiles
        energized_map = [[set() for _ in range(len(line))] for line in map]
        traverse_map((len(map) - 1, col) , 'n')
        num_energized_tiles = count_energized_tiles(energized_map)
        if num_energized_tiles > max_num_energized_tiles:
            max_num_energized_tiles = num_energized_tiles
    
    print(max_num_energized_tiles)