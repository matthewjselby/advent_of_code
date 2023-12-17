with open('./input.txt') as data:
    map = [list(line.strip()) for line in data.readlines()]

    def rotate_map():
        global map
        # tilt north
        for row in range(1, len(map)):
            for col in range(len(map[row])):
                if map[row][col] == 'O':
                    row_t = row - 1
                    while row_t >= 0 and map[row_t][col] == '.':
                        map[row_t][col] = 'O'
                        map[row_t + 1][col] = '.'
                        row_t -= 1
        # tilt west
        for row in range(len(map)):
            for col in range(1, len(map[row])):
                if map[row][col] == 'O':
                    col_t = col - 1
                    while col_t >= 0 and map[row][col_t] == '.':
                        map[row][col_t] = 'O'
                        map[row][col_t + 1] = '.'
                        col_t -= 1
        # tilt south
        for row in range(len(map) - 2, -1, -1):
            for col in range(len(map[row])):
                if map[row][col] == 'O':
                    row_t = row + 1
                    while row_t < len(map) and map[row_t][col] == '.':
                        map[row_t][col] = 'O'
                        map[row_t - 1][col] = '.'
                        row_t += 1
        # tilt east
        for row in range(len(map)):
            for col in range(len(map[row]) - 2, -1, -1):
                if map[row][col] == 'O':
                    col_t = col + 1
                    while col_t < len(map[row]) and map[row][col_t] == '.':
                        map[row][col_t] = 'O'
                        map[row][col_t - 1] = '.'
                        col_t += 1


    import pickle
    seen_maps = {pickle.dumps(map)}
    prev_maps_lst = [pickle.dumps(map)]

    for i in range(1000000000):
        rotate_map()
        if (pickled_map := pickle.dumps(map)) not in seen_maps:
            seen_maps.add(pickled_map)
            prev_maps_lst.append(pickled_map)
        else:
            break
    
    cycle_end = i + 1
    cycle_start = prev_maps_lst.index(pickle.dumps(map))
    matching_index = (1000000000 - cycle_start) % (cycle_end - cycle_start) + cycle_start
    matching_map = pickle.loads(prev_maps_lst[matching_index])

    # calculate load on north beams
    total_load = 0
    for row in range(len(matching_map)):
        for col in range(len(matching_map[row])):
            if matching_map[row][col] == 'O':
                total_load += len(map) - row
    print(total_load)
    