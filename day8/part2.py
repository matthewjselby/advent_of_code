import math

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
    
    target_nodes = []
    for node in nodes:
        if node.endswith('A'):
            target_nodes.append(node)

    distances = []
    for target_node in target_nodes:
        next_node = target_node
        steps = 0
        while not next_node.endswith('Z'):
            for instruction in instructions:
                next_node = nodes[next_node][instruction]
                steps += 1
        distances.append(steps)

    lcm_distances = 1
    for distance in distances:
        lcm_distances = lcm_distances * distance // math.gcd(lcm_distances, distance)
    print(lcm_distances)