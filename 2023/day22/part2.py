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

    supports_map = {brick_idx: set() for brick_idx in range(len(bricks))}
    supported_by_map = {brick_idx: set() for brick_idx in range(len(bricks))}
    support_bricks = set()

    for brick_idx, brick in enumerate(bricks):
        for l_brick_idx, brick_below in enumerate(bricks[:brick_idx]):
            if bricks_overlap(brick, brick_below) and brick_below[5] == brick[2] - 1:
                supports_map[l_brick_idx].add(brick_idx)
                supported_by_map[brick_idx].add(l_brick_idx)
        if len(supported_by_map[brick_idx]) == 1:
            support_bricks.update(supported_by_map[brick_idx])

    num_fallen_bricks = 0

    for support_brick in support_bricks:
        fallen_bricks = set([support_brick])
        for supported_brick in supported_by_map:
            if len(supported_by_map[supported_brick]) > 0 and supported_by_map[supported_brick].issubset(fallen_bricks):
                fallen_bricks.add(supported_brick)
        num_fallen_bricks += len(fallen_bricks) - 1

    print(num_fallen_bricks)
        
                

    

