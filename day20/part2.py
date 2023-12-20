import math

with open('./input.txt') as data:
    module_map = {}
    back_refs = {}
    conj_modules = []
    all_modules = set()
    for line in data.readlines():
        parts = line.strip().split(' -> ')
        if parts[0] == 'broadcaster':
            module_map['broadcaster'] = ('broadcaster', {}, tuple(parts[1].split(', ')))
            continue
        module_type = parts[0][0]
        module_state = {}
        module_name = parts[0][1:].strip()
        downstream_modules = tuple(parts[1].split(', '))
        for downstream_module in downstream_modules:
            if not downstream_module in back_refs:
                back_refs[downstream_module] = [module_name]
            else:
                back_refs[downstream_module].append(module_name)
            all_modules.add(downstream_module)
        if module_type == '%':
            module_state['state'] = 'off'
        elif module_type == '&':
            module_state['input_state_map'] = {}
            conj_modules.append(module_name)
        module_map[module_name] = (module_type, module_state, downstream_modules)
    
    for module in all_modules:
        if not module in module_map:
            module_map[module] = ('output', {}, ())

    for conj_module in conj_modules:
        for back_ref in back_refs[conj_module]:
            module_map[conj_module][1]['input_state_map'][back_ref] = 'low'

    nodes_to_watch = back_refs[back_refs['rx'][0]]
    print(nodes_to_watch)

    def send_pulse():
        pulse_queue = [('broadcaster', 'low', None)]
        while len(pulse_queue) > 0:
            module_name, pulse, sender = pulse_queue.pop(0)
            module_type, module_state, downstream_modules = module_map[module_name]
            if module_type == '%':
                if pulse == 'low':
                    if module_state['state'] == 'off':
                        module_state['state'] = 'on'
                        pulse = 'high'
                    else:
                        module_state['state'] = 'off'
                        pulse = 'low'
                else:
                    continue
            elif module_type == '&':
                module_state['input_state_map'][sender] = pulse
                num_low_inputs = len(list(filter(lambda x: x == 'low', module_state['input_state_map'].values())))
                if num_low_inputs == 0:
                    pulse = 'low'
                else:
                    pulse = 'high'
            elif module_type == 'output':
                continue
            if module_name in nodes_to_watch and pulse == 'high':
                nodes_to_watch.remove(module_name)
                return module_name
            for downstream_module in downstream_modules:
                pulse_queue.append((downstream_module, pulse, module_name))
        return ''

    intervals = []
    num_presses = 0
    while len(nodes_to_watch) > 0:
        num_presses += 1
        module_high = send_pulse()
        print(num_presses, end='\r')
        if module_high != '':
            print(f'module interval {num_presses} found for {module_high}')
            intervals.append(num_presses)
    lcm = 1
    for interval in intervals:
        lcm = lcm * interval // math.gcd(lcm, interval)
    print(lcm)
