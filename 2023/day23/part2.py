with open('./input.txt') as data:
    map = [list(line.strip()) for line in data.readlines()]
    num_rows = len(map)
    num_cols = len(map[0])

    start_position = (0, 0)
    for tile_idx, tile in enumerate(map[0]):
        if tile == '.':
            start_position = (0, tile_idx)
            break
    
    end_position = (0, 0)
    for tile_idx, tile in enumerate(map[-1]):
        if tile == '.':
            end_position = (num_rows - 1, tile_idx)
            break
    
    # find junctions
    
    nodes_to_visit = [start_position]
    visited_nodes = set()
    junctions = [start_position, end_position]

    while len(nodes_to_visit) > 0:
        current_row, current_col = nodes_to_visit.pop(0)
        visited_nodes.add((current_row, current_col))
        num_neighbors = 0
        for row_add, col_add in [(1, 0), (-1, 0), (0, 1), (0,-1)]:
            next_row = current_row + row_add
            next_col = current_col + col_add
            if (next_row, next_col) not in visited_nodes and 0 <= next_row < num_rows and 0 <= next_col < num_cols and map[next_row][next_col] != '#':
                num_neighbors += 1
                nodes_to_visit.append((next_row, next_col))
        if num_neighbors > 1:
            junctions.append((current_row, current_col))

    # build graph from points of interest (junctions)

    graph = {junction: {} for junction in junctions}

    for junction in junctions:
        junction_row, junction_col = junction
        nodes_to_visit = [(0, junction_row, junction_col)]
        visited_nodes = set()

        while len(nodes_to_visit) > 0:
            weight, current_row, current_col = nodes_to_visit.pop(0)
            visited_nodes.add((current_row, current_col))

            if weight != 0 and (current_row, current_col) in junctions:
                graph[(junction_row, junction_col)][(current_row, current_col)] = weight
                continue

            for row_add, col_add in [(1, 0), (-1, 0), (0, 1), (0,-1)]:
                next_row = current_row + row_add
                next_col = current_col + col_add
                if (next_row, next_col) not in visited_nodes and 0 <= next_row < num_rows and 0 <= next_col < num_cols and map[next_row][next_col] != '#':
                    nodes_to_visit.append((weight + 1, next_row, next_col))

    # perform dfs on the shortened graph to find longest path
                    
    def traverse_graph(current_node, path_length = 0, visited_nodes = set()):
        if current_node == end_position:
            return path_length
        visited_nodes = visited_nodes.copy()
        visited_nodes.add(current_node)
        longest_path = 0
        for neighbor, distance in graph[current_node].items():
            if not neighbor in visited_nodes:
                longest_path = max(longest_path, traverse_graph(neighbor, path_length + distance, visited_nodes))
        return longest_path
    
    print(traverse_graph(start_position))