import re

with open('./input.txt') as data:
    lines = data.readlines()
    num_regex = re.compile(r'[0-9]{1,}')
    times = list(map(lambda x: int(x), num_regex.findall(lines[0])))
    records = list(map(lambda x: int(x), num_regex.findall(lines[1])))
    ways_to_win = 1
    for i in range(len(times)):
        time = times[i]
        record = records[i]
        first_win = 0
        for s in range(1, time + 1):
            if s * (time - s) > record:
                first_win = s
                break
        ways_to_win *= time - (first_win * 2) + 1
    print(ways_to_win)