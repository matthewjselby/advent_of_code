with open('./input.txt') as data:
    workflows = {}
    workflows_parsed = False
    parts = []

    for line in data.readlines():
        # parse input
        if line == '\n':
            workflows_parsed = True
        elif not workflows_parsed:
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
        else:
            line = line.strip()
            part_attributes = {}
            for raw_part_attribute in line[1:-1].split(','):
                attribute_name = raw_part_attribute.split('=')[0]
                attribute_value = int(raw_part_attribute.split('=')[1])
                part_attributes[attribute_name] = attribute_value
            parts.append(part_attributes)

    accepted_parts = []

    # function to send a part through a given workflow
    def evaluate_workflow(workflow_name, part):
        workflow = workflows[workflow_name]
        for rule in workflow:
            condition, dest = rule
            if eval(condition, {}, part):
                    if dest == 'A':
                        accepted_parts.append(part)
                        break
                    elif dest == 'R':
                        break
                    else:
                        evaluate_workflow(dest, part)
                        break
    
    # evaluate rules on parts
    for part in parts:
        evaluate_workflow('in', part)

    # add up accepted parts values
    total_ratings = 0
    for accepted_part in accepted_parts:
        for attribute, value in accepted_part.items():
            total_ratings += value
    print(total_ratings)

