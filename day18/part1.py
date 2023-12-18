with open('./input.txt') as data:
    lines = data.readlines()
    dir_map = {
        'R': (0, 1),
        'L': (0, -1),
        'U': (-1, 0),
        'D': (1, 0)
    }
    dig_coords = []
    min_row = max_row = cur_row = 0
    min_col = max_col = cur_col = 0
    for line in lines:
        dir = line.strip().split(' ')[0]
        num_steps = int(line.strip().split(' ')[1])

        row_add, col_add = dir_map[dir]
        for _ in range(num_steps):
            cur_row += row_add
            cur_col += col_add
            dig_coords.append((cur_row, cur_col))
            if cur_row > max_row:
                max_row = cur_row
            if cur_row < min_row:
                min_row = cur_row
            if cur_col > max_col:
                max_col = cur_col
            if cur_col < min_col:
                min_col = cur_col
    
    num_rows = max_row - min_row + 1
    num_cols = max_col - min_col + 1
    dig_map = [['.' for _ in range(num_cols)] for _ in range(num_rows)]
    
    for dig_coord in dig_coords:
        dig_row = dig_coord[0] - min_row
        dig_col = dig_coord[1] - min_col
        dig_map[dig_row][dig_col] = '#'

    pit_capacity = 0
    for row_idx, row in enumerate(dig_map):
        for col_idx, col in enumerate(row):
            if col == '#':
                pit_capacity += 1
            else:
                n_col_idx = col_idx + 1
                edges_crossed = 0
                if n_col_idx >= len(row):
                    n_col_idx = col_idx - 1
                for t_row in dig_map[row_idx + 1:]:
                    if t_row[col_idx] == t_row[n_col_idx] == '#':
                        edges_crossed += 1
                if edges_crossed % 2 != 0:
                    pit_capacity += 1
                    
    print(pit_capacity)




        

