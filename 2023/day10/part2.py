from enum import Enum
import typing

_E = typing.TypeVar('_E', bound=Enum)

class Direction(Enum):
    north = (-1, 0)
    south = (1, 0)
    east = (0, 1)
    west = (0, -1)

    def opposite(self) -> _E:
        if self == Direction.north:
            return Direction.south
        elif self == Direction.south:
            return Direction.north
        elif self == Direction.east:
            return Direction.west
        elif self == Direction.west:
            return Direction.east

_G = typing.TypeVar('_G', bound="GridPosition")

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

    def move_direction(self, direction: Direction):
        row, col = direction.value
        self.row += row
        self.col += col

    def get_position_in_direction(self, direction: Direction) -> _G:
        row, col = direction.value
        return GridPosition(self.row + row, self.col + col)


class Grid:
    def __init__(self, grid: [str]) -> None:
        self.grid = grid
        self.num_rows = len(grid)
        self.num_cols = len(grid[0])
        self.shadow_grid = [['.' for _ in range(self.num_cols - 1)] for _ in range(self.num_rows)]
        self.loop_start = self.get_starting_position()

    def get_starting_position(self) -> GridPosition:
        starting_position = GridPosition(0, 0)
        for row in range(self.num_rows):
            start_found = False
            for col in range(self.num_cols):
                if self.grid[row][col] == 'S':
                    starting_position = GridPosition(row, col)
                    start_found = True
                    break
            if start_found:
                break
        self.shadow_grid[starting_position.row][starting_position.col] = 1
        return starting_position
    
    def available_entry_directions_to(self, position: GridPosition) -> typing.Set[_E]:
        current_pipe = self.grid[position.row][position.col]
        if current_pipe == '|':
            return set([Direction.north, Direction.south])
        elif current_pipe == '-':
            return set([Direction.east, Direction.west])
        elif current_pipe == 'F':
            return set([Direction.west, Direction.north])
        elif current_pipe == '7':
            return set([Direction.east, Direction.north])
        elif current_pipe == 'J':
            return set([Direction.east, Direction.south])
        elif current_pipe == 'L':
            return set([Direction.west, Direction.south])
        elif current_pipe == 'S':
            return set([Direction.north, Direction.south, Direction.east, Direction.west])
        else:
            return set()
    
    def available_exit_directions_from(self, position: GridPosition) -> typing.Set[_E]:
        current_pipe = self.grid[position.row][position.col]
        if current_pipe == '|':
            return set([Direction.north, Direction.south])
        elif current_pipe == '-':
            return set([Direction.east, Direction.west])
        elif current_pipe == 'F':
            return set([Direction.east, Direction.south])
        elif current_pipe == '7':
            return set([Direction.west, Direction.south])
        elif current_pipe == 'J':
            return set([Direction.north, Direction.west])
        elif current_pipe == 'L':
            return set([Direction.east, Direction.north])
        elif current_pipe == 'S':
            return set([Direction.north, Direction.south, Direction.east, Direction.west])
        else:
            return set()
        
    def available_move_directions_from(self, position: GridPosition) -> typing.Set[_E]:
        available_exit_directions = self.available_exit_directions_from(position)
        available_directions = set()
        for available_exit_direction in available_exit_directions:
            position_in_direction = position.get_position_in_direction(available_exit_direction)
            available_entry_directions = self.available_entry_directions_to(position_in_direction)
            if available_exit_direction in available_entry_directions:
                available_directions.add(available_exit_direction)
        return available_directions

    def traverse_loop(self):
        # get into loop from starting position
        current_position = self.loop_start.copy()
        move_direction = self.available_move_directions_from(current_position).pop()
        from_direction = move_direction.opposite()
        current_position.move_direction(move_direction)
        pos_idx = 2
        while current_position != self.loop_start:
            self.shadow_grid[current_position.row][current_position.col] = pos_idx
            move_direction = self.available_move_directions_from(current_position).difference(set([from_direction])).pop()
            from_direction = move_direction.opposite()
            current_position.move_direction(move_direction)
            pos_idx += 1
    
    def get_expanded_grid(self):
        expanded_grid = [['.' if col % 2 == 0 and row % 2 == 0 else ' ' for col in range(self.num_cols + (self.num_cols - 1))] for row in range(self.num_rows + (self.num_rows - 1))]
        expanded_grid[self.loop_start.row * 2][self.loop_start.col * 2] = 'x'
        # get into loop from starting position
        current_position = self.loop_start.copy()
        move_direction = self.available_move_directions_from(current_position).pop()
        from_direction = move_direction.opposite()
        current_position.move_direction(move_direction)
        pos_idx = 2
        while current_position != self.loop_start:
            expanded_grid[current_position.row * 2][current_position.col * 2] = 'x'
            expanded_grid[current_position.row * 2 + from_direction.value[0]][current_position.col * 2 + from_direction.value[1]] = 'x'
            move_direction = self.available_move_directions_from(current_position).difference(set([from_direction])).pop()
            from_direction = move_direction.opposite()
            current_position.move_direction(move_direction)
            pos_idx += 1
        expanded_grid[current_position.row * 2 + from_direction.value[0]][current_position.col * 2 + from_direction.value[1]] = 'x'
        return expanded_grid

with open('./input.txt') as data:
    grid = Grid(data.readlines())
    expanded_grid = grid.get_expanded_grid()
    num_enclosed = 0
    for row in range(1, len(expanded_grid) - 1):
        for col in range(1, len(expanded_grid[row]) - 1):
            if expanded_grid[row][col] == '.':
                s_row = row - 1
                num_edges = 0
                while s_row >= 0:
                    if expanded_grid[s_row][col - 1] == 'x':
                        num_edges += 1
                    s_row -= 1
                if num_edges % 2 != 0:
                    num_enclosed += 1
    print(num_enclosed)