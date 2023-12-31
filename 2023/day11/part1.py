with open('./input.txt') as data:
    galaxy_map = [list(line.strip()) for line in data.readlines()]
    # expand the image - doubling any rows not containing galaxies
    row_offset = 0
    for row_num in range(len(galaxy_map)):
        if '#' not in galaxy_map[row_num + row_offset]:
            galaxy_map.insert(row_num + row_offset, list(galaxy_map[row_num + row_offset]))
            row_offset += 1
    # expand the image - doubling any columns not containing galaxies
    cols_to_add = []
    for col_num in range(len(galaxy_map[0])):
        col = [row[col_num] for row in galaxy_map]
        if '#' not in col:
            cols_to_add.append(col_num)
    for row_num in range(len(galaxy_map)):
        col_offset = 0
        for col_to_add in cols_to_add:
            galaxy_map[row_num].insert(col_to_add + col_offset, '.')
            col_offset += 1
    combined_path_lengths = 0
    # find the galaxies and traverse the map finding other galaxies
    for row_num in range(len(galaxy_map)):
        for col_num in range(len(galaxy_map[row_num])):
            if galaxy_map[row_num][col_num] == '#':
                n_col = col_num + 1
                while n_col < len(galaxy_map[0]):
                    if galaxy_map[row_num][n_col] == '#':
                        combined_path_lengths += abs(n_col - col_num)
                    n_col += 1
                n_row = row_num + 1
                while n_row < len(galaxy_map):
                    if galaxy_map[n_row][col_num] == '#':
                        combined_path_lengths += abs(n_row - row_num)
                    n_col = col_num - 1
                    while n_col >= 0:
                        if galaxy_map[n_row][n_col] == '#':
                            combined_path_lengths += abs(n_row - row_num) + abs(n_col - col_num)
                        n_col -= 1
                    n_col = col_num + 1
                    while n_col < len(galaxy_map[0]):
                        if galaxy_map[n_row][n_col] == '#':
                            combined_path_lengths += abs(n_row - row_num) + abs(n_col - col_num)
                        n_col += 1
                    n_row += 1
    print(combined_path_lengths)
