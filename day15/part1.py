with open('./input.txt') as data:
    hash_sum = 0
    for str in data.read().strip().split(','):
        # perform hash algorithm
        current_val = 0
        for c in str:
            current_val += ord(c)
            current_val *= 17
            current_val = current_val % 256
        hash_sum += current_val
    print(hash_sum)