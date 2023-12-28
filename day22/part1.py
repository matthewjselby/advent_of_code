with open('./input.txt') as data:
    bricks = [list(map(int, line.replace('~', ',').split(','))) for line in data.readlines()]
    bricks.sort(key=lambda x: x[2])

    def bricks_overlap(brick1, brick2):
        return max(brick1[0], brick2[0]) <= min(brick1[3], brick2[3]) and max(brick1[1], brick2[1]) <= min(brick1[4], brick2[4])
    
    for brick_idx, brick in enumerate(bricks):
        brick_floor = 1
        for lower_brick in bricks[:brick_idx]:
            if bricks_overlap(brick, lower_brick):
                brick_floor = max(brick_floor, lower_brick[5] + 1)
        brick[5] -= brick[2] - brick_floor
        brick[2] = brick_floor
    
    bricks.sort(key=lambda x: x[2])
    
    bricks_copy = bricks.copy()

    for brick_idx, brick in enumerate(bricks):
        supporting_bricks = []
        for brick_below in reversed(bricks[:brick_idx]):
            if bricks_overlap(brick, brick_below) and brick_below[5] == brick[2] - 1:
                supporting_bricks.append(brick_below)
        if len(supporting_bricks) == 1:
            if supporting_bricks[0] in bricks_copy:
                bricks_copy.remove(supporting_bricks[0])
        

    print(len(bricks_copy))