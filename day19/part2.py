from copy import deepcopy

with open('./input.txt') as data:
    workflows = {}

    for line in data.readlines():
        # parse input
        if line == '\n':
            break
        line = line.strip()
        workflow_name = line.split('{')[0]
        raw_rules = line[len(workflow_name) + 1:-1].split(',')
        parsed_rules = []
        for raw_rule in raw_rules:
            if len(split_rule := raw_rule.split(':')) > 1:
                parsed_rules.append((split_rule[0], split_rule[1]))
            else:
                parsed_rules.append(('True', raw_rule))
        workflows[workflow_name] = parsed_rules

    def count_combos(acceptable_ranges, workflow_name = 'in'):
        if workflow_name == 'R':
            return 0
        if workflow_name == 'A':
            num_combos = 1
            for low, high in acceptable_ranges.values():
                num_combos *= high - low + 1
            return num_combos
        
        rules = workflows[workflow_name]
        num_combos = 0

        for cond, dest in rules:
            if cond == 'True':
                num_combos += count_combos(acceptable_ranges, dest)
            else:
                var = cond[0]
                cmp = cond[1]
                val = int(cond[2:])
                low, high = acceptable_ranges[var]
                true_range = (low, val - 1) if cmp == '<' else (val + 1, high)
                false_range = (val, high) if cmp == '<' else (low, val)
                if true_range[0] <= true_range[1]:
                    acceptable_ranges_copy = dict(acceptable_ranges)
                    acceptable_ranges_copy[var] = true_range
                    num_combos += count_combos(acceptable_ranges_copy, dest)
                if false_range[0] <= false_range[1]:
                    acceptable_ranges = dict(acceptable_ranges)
                    acceptable_ranges[var] = false_range
                else:
                    break

        return num_combos 


    acceptable_ranges = {key: (1, 4000) for key in 'xmas'}
    print(count_combos(acceptable_ranges))


