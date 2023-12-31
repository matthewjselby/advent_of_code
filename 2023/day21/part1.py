with open('./test_data.txt') as data:
    # parse input data
    garden_map = [list(line.strip()) for line in data.readlines()]
    
    # find starting position
    starting_position = (0, 0)
    for row in range(len(garden_map)):
        for col in range(len(garden_map[row])):
            if garden_map[row][col] == 'S':
                starting_position = (row, col)
    
    # find all visitable plots
    reachable_plots = set()
    visited_plots = set(starting_position)
    plots_to_see = [(starting_position, 203)]

    while len(plots_to_see) > 0:
        current_position, steps_remaining = plots_to_see.pop(0)
        if steps_remaining % 2 == 0:
            reachable_plots.add(current_position)
        if steps_remaining == 0:
            continue
        curr_row, curr_col = current_position
        for next_row, next_col in [(curr_row - 1, curr_col), (curr_row + 1, curr_col), (curr_row, curr_col - 1), (curr_row, curr_col + 1)]:
            if next_row < 0 or next_row >= len(garden_map) or next_col < 0 or next_col >= len(garden_map[0]):
                continue
            if garden_map[next_row][next_col] != '#' and (next_row, next_col) not in visited_plots:
                visited_plots.add((next_row, next_col))
                plots_to_see.append(((next_row, next_col), steps_remaining - 1))

    print(len(reachable_plots))

