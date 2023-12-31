with open('./input.txt') as input:
    lines = input.readlines()
    total = 0
    for line in lines:
        l = 0
        r = -1
        while not line[l].isdigit():
            l += 1
        while not line[r].isdigit():
            r -= 1
        total += (int(line[l]) * 10) + int(line[r])
    print(total)
