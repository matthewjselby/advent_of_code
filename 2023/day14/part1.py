with open('./input.txt') as data:
    rock_map = [list(line.strip()) for line in data.readlines()]
    # move all rocks as far north as possible
    for row in range(1, len(rock_map)):
        for col in range(len(rock_map[row])):
            if rock_map[row][col] == 'O':
                row_t = row - 1
                while row_t >= 0 and rock_map[row_t][col] not in 'O#':
                    rock_map[row_t + 1][col] = '.'
                    rock_map[row_t][col] = 'O'
                    row_t -= 1
    # calculate load on north beams
    total_load = 0
    for row in range(len(rock_map)):
        for col in range(len(rock_map[row])):
            if rock_map[row][col] == 'O':
                total_load += len(rock_map) - row
    print(total_load)
