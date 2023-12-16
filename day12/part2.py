cache = {}

def count_perms(pattern, groups):
    if groups == ():
        return 1 if '#' not in pattern else 0
    
    if pattern == '':
        return 1 if groups == () else 0
    
    key = (pattern, groups)

    if key in cache:
        return cache[key]

    num_perms = 0

    if pattern[0] == '.' or pattern[0] == '?':
        num_perms += count_perms(pattern[1:], groups)
    
    if pattern[0] == '#' or pattern[0] == '?':
        if groups[0] <= len(pattern) and '.' not in pattern[:groups[0]] and (groups[0] == len(pattern) or pattern[groups[0]] != '#'):
            num_perms += count_perms(pattern[groups[0] + 1:], groups[1:])

    cache[key] = num_perms

    return num_perms

with open('./input.txt') as data:
    lines = data.readlines()
    num_perms = 0
    for line in lines:
        pattern = line.strip().split(' ')[0]
        groups = tuple(map(lambda x: int(x), line.strip().split(' ')[1].split(',')))
        expanded_pattern = pattern + (('?' + pattern) * 4)
        expanded_groups = groups * 5
        num_perms += count_perms(expanded_pattern, expanded_groups)
    print(num_perms)