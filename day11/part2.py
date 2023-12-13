with open('./input.txt') as data:
    galaxy_map = [list(line.strip()) for line in data.readlines()]
    # find all the empty rows
    empty_space_multiplier = 1000000
    empty_rows = set()
    for row_num in range(len(galaxy_map)):
        if '#' not in galaxy_map[row_num]:
            empty_rows.add(row_num)
    # find all the empty columns
    empty_cols = set()
    for col_num in range(len(galaxy_map[0])):
        col = [row[col_num] for row in galaxy_map]
        if '#' not in col:
            empty_cols.add(col_num)
    combined_path_lengths = 0
    # find the galaxies and traverse the map finding other galaxies
    for row_num in range(len(galaxy_map)):
        for col_num in range(len(galaxy_map[row_num])):
            if galaxy_map[row_num][col_num] == '#':
                n_col = col_num + 1
                while n_col < len(galaxy_map[0]):
                    if galaxy_map[row_num][n_col] == '#':
                        path_length = abs(n_col - col_num)
                        traversed_cols = set(range(col_num, n_col + 1))
                        num_empty_cols_traversed = len(empty_cols.intersection(traversed_cols))
                        if num_empty_cols_traversed > 0:
                            path_length += (num_empty_cols_traversed * empty_space_multiplier) - num_empty_cols_traversed
                        combined_path_lengths += path_length
                        # print(f'Path found between {row_num}, {col_num} and {row_num}, {n_col} - path length: {path_length}')
                        # print(f'Num empty cols traversed: {num_empty_cols_traversed}')
                    n_col += 1
                n_row = row_num + 1
                while n_row < len(galaxy_map):
                    if galaxy_map[n_row][col_num] == '#':
                        path_length = abs(n_row - row_num)
                        traversed_rows = set(range(row_num, n_row + 1))
                        num_empty_rows_traversed = len(empty_rows.intersection(traversed_rows))
                        if num_empty_rows_traversed > 0:
                            path_length += (num_empty_rows_traversed * empty_space_multiplier) - num_empty_rows_traversed
                        combined_path_lengths += path_length
                        # print(f'Path found between {row_num}, {col_num} and {n_row}, {col_num} - path length: {path_length}')
                        # print(f'Num empty rows traversed: {num_empty_rows_traversed}')
                    n_col = col_num - 1
                    while n_col >= 0:
                        if galaxy_map[n_row][n_col] == '#':
                            path_length = abs(n_row - row_num) + abs(n_col - col_num)
                            traversed_cols = set(range(n_col, col_num + 1))
                            num_empty_cols_traversed = len(empty_cols.intersection(traversed_cols))
                            traversed_rows = set(range(row_num, n_row + 1))
                            num_empty_rows_traversed = len(empty_rows.intersection(traversed_rows))
                            if num_empty_rows_traversed > 0:
                                path_length += (num_empty_rows_traversed * empty_space_multiplier) - num_empty_rows_traversed
                            if num_empty_cols_traversed > 0:
                                path_length += (num_empty_cols_traversed * empty_space_multiplier) - num_empty_cols_traversed
                            combined_path_lengths += path_length
                            # print(f'Path found between {row_num}, {col_num} and {n_row}, {n_col} - path length: {path_length}')
                            # print(f'Num empty cols traversed: {num_empty_cols_traversed} | rows: {num_empty_rows_traversed}')
                        n_col -= 1
                    n_col = col_num + 1
                    while n_col < len(galaxy_map[0]):
                        if galaxy_map[n_row][n_col] == '#':
                            path_length = abs(n_row - row_num) + abs(n_col - col_num)
                            traversed_cols = set(range(col_num, n_col + 1))
                            num_empty_cols_traversed = len(empty_cols.intersection(traversed_cols))
                            traversed_rows = set(range(row_num, n_row + 1))
                            num_empty_rows_traversed = len(empty_rows.intersection(traversed_rows))
                            if num_empty_rows_traversed > 0:
                                path_length += (num_empty_rows_traversed * empty_space_multiplier) - num_empty_rows_traversed
                            if num_empty_cols_traversed > 0:
                                path_length += (num_empty_cols_traversed * empty_space_multiplier) - num_empty_cols_traversed
                            combined_path_lengths += path_length
                            # print(f'Path found between {row_num}, {col_num} and {n_row}, {n_col} - path length: {path_length}')
                            # print(f'Num empty cols traversed: {num_empty_cols_traversed} | rows: {num_empty_rows_traversed}')
                        n_col += 1
                    n_row += 1
    print(combined_path_lengths)
