import sys
sys.setrecursionlimit(5000)

with open('./input.txt') as data:
    map = [list(line.strip()) for line in data.readlines()]
    num_rows = len(map)
    num_cols = len(map[0])

    starting_position = (0, 0)
    for tile_idx, tile in enumerate(map[0]):
        if tile == '.':
            starting_position = (0, tile_idx)
            break


    def traverse_path(current_position, visited_tiles = set()):
        current_row, current_col = current_position
        if current_row == num_rows - 1:
            return 0
        current_tile = map[current_row][current_col]
        visited_tiles = visited_tiles.copy()
        visited_tiles.add(current_position)
        dirs = []
        if current_tile == '^':
            dirs = [(-1, 0)]
        elif current_tile == '>':
            dirs = [(0, 1)]
        elif current_tile == 'v':
            dirs = [(1, 0)]
        elif current_tile == '<':
            dirs = [(0, -1)]
        else:
            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        max_path_length = 0
        for row_add, col_add in dirs:
            next_row = current_row + row_add
            next_col = current_col + col_add
            if (next_row, next_col) not in visited_tiles and 0 <= next_row < num_rows and 0 <= next_col < num_cols and map[next_row][next_col] != '#':
                path_length = traverse_path((next_row, next_col), visited_tiles)
                max_path_length = max(max_path_length, path_length)
        return max_path_length + 1

    print(traverse_path(starting_position))