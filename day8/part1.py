with open('./input.txt') as data:
    lines = data.readlines()
    instructions = lines.pop(0).strip()
    lines.pop(0)
    nodes = {}
    for line in lines:
        node = line.split(' = ')[0]
        l = line.split(' = ')[1].split(', ')[0].strip()[1:]
        r = line.split(' = ')[1].split(', ')[1].strip()[:-1]
        nodes[node] = {"L": l, "R": r}

    next_node = 'AAA'
    steps = 0
    while next_node != 'ZZZ':
        for instruction in instructions:
            next_node = nodes[next_node][instruction]
            steps += 1
    print(steps)