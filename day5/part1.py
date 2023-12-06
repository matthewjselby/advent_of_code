with open('./input.txt') as data:
    lines = data.readlines()
    seeds_to_plant = list(map(lambda x: int(x), lines.pop(0).split(': ')[1].split(' ')))
    master_map = {}
    current_mapping = ""
    for line in lines:
        line = line.strip()
        if line.endswith(':'):
            current_mapping = line.split(' ')[0]
            master_map[current_mapping] = []
        elif len(line) == 0:
            pass
        elif line[0].isdigit():
            master_map[current_mapping].append(list(map(lambda x: int(x), line.split(' '))))
    locations = []
    for seed_to_plant in seeds_to_plant:
        seed_info = [seed_to_plant]
        for map_key in master_map:
            mapping_found = False
            for mapping in master_map[map_key]:
                if mapping[1] <= seed_info[-1] < mapping[1] + mapping[2]:
                    seed_info.append(mapping[0] + (seed_info[-1] - mapping[1]))
                    mapping_found = True
                    break
            if not mapping_found:
                seed_info.append(seed_info[-1])
        locations.append(seed_info[-1])
    print(min(locations))
            
