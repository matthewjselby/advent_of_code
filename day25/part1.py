import collections

with open('./input.txt') as data:
    component_graph = collections.defaultdict(set)
    edges = set()
    for line in data.readlines():
        component, *connected_components = line.strip().replace(':', '').split()
        for connected_component in connected_components:
            component_graph[component].add(connected_component)
            component_graph[connected_component].add(component)
    
    sub_graph = set(component_graph)

    count = lambda component: len(component_graph[component] - sub_graph)

    while sum(map(count, sub_graph)) != 3:
        sub_graph.remove(max(sub_graph, key=count))

    print(len(sub_graph) * len(set(component_graph) - sub_graph))