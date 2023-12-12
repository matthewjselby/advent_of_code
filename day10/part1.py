class GridPosition:
    def __init__(self, row, col) -> None:
        self.row = row
        self.col = col

    def __repr__(self) -> str:
        return f'({self.row}, {self.col})'
    
    def copy(self):
        return GridPosition(self.row, self.col)
    
    def __eq__(self, __value: object) -> bool:
        return self.row == __value.row and self.col == __value.col
    
    def move_north(self):
        self.row -= 1

    def move_south(self):
        self.row += 1

    def move_east(self):
        self.col += 1

    def move_west(self):
        self.col -= 1

def move_next(previous_position, current_position):
        current_tile = grid[current_position.row][current_position.col]
        next_position = current_position.copy()
        if current_tile == '|':
            if previous_position.row < next_position.row:
                next_position.move_south()
            else:
                next_position.move_north()
        elif current_tile == '-':
            if previous_position.col < next_position.col:
                next_position.move_east()
            else:
                next_position.move_west()
        elif current_tile == 'L':
            if previous_position.col > next_position.col:
                next_position.move_north()
            else:
                next_position.move_east()
        elif current_tile == 'J':
            if previous_position.col < next_position.col:
                next_position.move_north()
            else:
                next_position.move_west()
        elif current_tile == '7':
            if previous_position.col < next_position.col:
                next_position.move_south()
            else:
                next_position.move_west()
        elif current_tile == 'F':
            if previous_position.col > next_position.col:
                next_position.move_south()
            else:
                next_position.move_east()
        return current_position, next_position


with open('./input.txt') as data:
    grid = data.readlines()
    num_rows = len(grid)
    num_cols = len(grid[0])
    # look for starting position
    starting_position = GridPosition(0, 0)
    for row in range(num_rows):
        start_found = False
        for col in range(num_cols):
            if grid[row][col] == 'S':
                starting_position = GridPosition(row, col)
                start_found = True
                break
        if start_found:
            break
    # get into loop from starting position
    current_position = starting_position.copy()
    if col < num_cols - 1 and grid[row][col + 1] in set(['7', '-', 'J']):
        current_position.move_east()
    elif row < num_rows - 1 and grid[row + 1][col] in set(['L', 'J', '|']):
        current_position.move_south()
    elif col > 0 and grid[row][col - 1] in set(['L', 'F', '-']):
        current_position.move_west()
    elif row > 0 and grid[row - 1][col] in set(['|', 'F', '7']):
        current_position.move_north()
    previous_position = starting_position.copy()
    total_steps = 1
    while current_position != starting_position:
        print(f'Moving from {previous_position} to {current_position}')
        previous_position, current_position = move_next(previous_position, current_position)
        total_steps += 1
    print(total_steps // 2)

    
    
