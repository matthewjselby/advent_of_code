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

    def send_pulse():
        pulse_queue = [('broadcaster', 'low', None)]
        high_pulses = low_pulses = 0
        while len(pulse_queue) > 0:
            module_name, pulse, sender = pulse_queue.pop(0)
            module_type, module_state, downstream_modules = module_map[module_name]
            if module_type == 'broadcaster':
                if pulse == 'low':
                    low_pulses += len(downstream_modules)
                else:
                    high_pulses += len(downstream_modules)
            elif module_type == '%':
                if pulse == 'low':
                    if module_state['state'] == 'off':
                        high_pulses += len(downstream_modules)
                        module_state['state'] = 'on'
                        pulse = 'high'
                    else:
                        low_pulses += len(downstream_modules)
                        module_state['state'] = 'off'
                        pulse = 'low'
                else:
                    continue
            elif module_type == '&':
                module_state['input_state_map'][sender] = pulse
                num_low_inputs = len(list(filter(lambda x: x == 'low', module_state['input_state_map'].values())))
                if num_low_inputs == 0:
                    low_pulses += len(downstream_modules)
                    pulse = 'low'
                else:
                    high_pulses += len(downstream_modules)
                    pulse = 'high'
            if module_type == 'output':
                continue
            for downstream_module in downstream_modules:
                print(f'{module_name} -{pulse}-> {downstream_module}')
                pulse_queue.append((downstream_module, pulse, module_name))
        return high_pulses, low_pulses + 1
        
    high_pulses = low_pulses = 0
    for _ in range(1000):
        high, low = send_pulse()
        print(high, low)
        high_pulses += high
        low_pulses += low
    print(high_pulses * low_pulses)