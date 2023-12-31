def pattern_matches_groups(pattern, groups):
    spring_groups = [len(x) for x in pattern.split('.') if len(x) > 0]
    return spring_groups == groups

def generate_perms(pattern):
    perms = []
    if pattern[0] == '?':
        perms = ['.', '#']
    else:
        perms = [pattern[0]]
    for pattern_idx in range(1, len(pattern)):
        if pattern[pattern_idx] == '?':
            new_perms = []
            for perm_idx in range(len(perms)):
                new_perms.append(perms[perm_idx] + '.')
                new_perms.append(perms[perm_idx] + '#')
            perms = new_perms
        else:
            for perm_idx in range(len(perms)):
                perms[perm_idx] += pattern[pattern_idx]
    return perms

with open('./input.txt') as data:
    lines = data.readlines()
    num_arrangements = 0
    for line in lines:
        pattern = line.strip().split(' ')[0]
        groups = list(map(lambda x: int(x), line.strip().split(' ')[1].split(',')))
        perms = generate_perms(pattern)
        for perm in perms:
            if pattern_matches_groups(perm, groups):
                num_arrangements += 1
    print(num_arrangements)
