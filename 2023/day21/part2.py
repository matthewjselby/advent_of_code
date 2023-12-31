import numpy as np

with open('./input.txt') as data:
    # parse input data
    garden_map = [list(line.strip()) for line in data.readlines()]
    
    # find starting position
    starting_position = (0, 0)
    for row in range(len(garden_map)):
        for col in range(len(garden_map[row])):
            if garden_map[row][col] == 'S':
                starting_position = (row, col)

    num_rows = len(garden_map)
    num_cols = len(garden_map[0])

    # find all reachable plots given a starting position and number of steps remaining
    def count_reachable_plots(starting_position, steps_remaining):
        reachable_plots = set()
        visited_plots = set()
        visited_plots.add(starting_position)
        plots_to_see = [(starting_position, steps_remaining)]

        while len(plots_to_see) > 0:
            current_position, steps_remaining = plots_to_see.pop(0)
            if steps_remaining % 2 == 0:
                reachable_plots.add(current_position)
            if steps_remaining == 0:
                continue
            curr_row, curr_col = current_position
            for next_row, next_col in [(curr_row - 1, curr_col), (curr_row + 1, curr_col), (curr_row, curr_col - 1), (curr_row, curr_col + 1)]:
                corr_row = next_row % num_rows
                corr_col = next_col % num_cols
                if garden_map[corr_row][corr_col] != '#' and (next_row, next_col) not in visited_plots:
                    visited_plots.add((next_row, next_col))
                    plots_to_see.append(((next_row, next_col), steps_remaining - 1))

        return len(reachable_plots)

    # find number of reachable plots at 65, 196, and 327
    points = [(i, count_reachable_plots(starting_position, 65 + i * 131)) for i in range(3)]

    # fit found points to a quadratic equation
    coefficients = np.polyfit(*zip(*points), 2)
    # interpolate answer
    print(round(np.polyval(coefficients, 202300)))