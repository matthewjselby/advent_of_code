with open('./input.txt') as data:
    min_row = row = 0
    min_col = col = 0

    num_digs = 0
    points = [(0, 0)]

    lines = data.readlines()
    for line in lines:
        num_steps = int(line.strip().split(' ')[2][2:7], 16)
        dir = int(line.strip().split(' ')[2][7])
        
        num_digs += num_steps

        if dir == 0:
            col += num_steps
        elif dir == 1:
            row += num_steps
        elif dir == 2:
            col -= num_steps
        elif dir == 3:
            row -= num_steps

        points.append((row, col))

        if row < min_row:
            min_row = row
        if col < min_col:
            min_col = col

    point_sum = 0
    for p_idx in range(1, len(points)):
        p1r, p1c = points[p_idx - 1]
        p1r -= min_row
        p1c -= min_col
        p2r, p2c = points[p_idx]
        p2r -= min_row
        p2c -= min_col
        point_sum += (p1c * p2r) - (p2c * p1r)
    print((point_sum // 2) + (num_digs // 2) + 1)
