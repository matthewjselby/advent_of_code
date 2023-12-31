from heapq import heappop, heappush

with open('./test_data.txt') as data:
    map = [list(map(lambda x: int(x), list(line.strip()))) for line in data.readlines()]
    num_rows = len(map)
    num_cols = len(map[0])

    def block_in_direction(row, col, dir):
        if dir == 'n':
            return (row - 1, col)
        if dir == 's':
            return (row + 1, col)
        if dir == 'e':
            return (row, col + 1)
        if dir == 'w':
            return (row, col - 1)
        
    def dir_opposite(dir):
        if dir == 'n':
            return 's'
        if dir == 's':
            return 'n'
        if dir == 'e':
            return 'w'
        if dir == 'w':
            return 'e'

    visited = set()
    # priority queue
    pq = []
    # put an entry in the queue for the top left block
    # format is heat loss, row, col, direction, number of steps in direction
    first_block = (0, 0, 0, 'e', 0)
    heappush(pq, first_block)

    while len(pq) > 0:
        heat_loss, row, col, dir, num_steps_in_dir = heappop(pq)

        if (row, col, dir, num_steps_in_dir) in visited:
            continue
        visited.add((row, col, dir, num_steps_in_dir))

        if row == len(map) - 1 and col == len(map[0]) - 1:
            print(heat_loss)
            break

        if num_steps_in_dir < 3:
            next_row, next_col = block_in_direction(row, col, dir)
            if 0 <= next_row < num_rows and 0 <= next_col < num_cols:
                new_block = (heat_loss + map[next_row][next_col], next_row, next_col, dir, num_steps_in_dir + 1)
                heappush(pq, new_block)

        for new_dir in set(['n', 's', 'e', 'w']).difference(set([dir, dir_opposite(dir)])):
            next_row, next_col = block_in_direction(row, col, new_dir)
            if 0 <= next_row < num_rows and 0 <= next_col < num_cols:
                new_block = (heat_loss + map[next_row][next_col], next_row, next_col, new_dir, 1)
                heappush(pq, new_block)