import re
from collections import OrderedDict

def hash_str(str):
    current_val = 0
    for c in str:
        current_val += ord(c)
        current_val *= 17
        current_val = current_val % 256
    return current_val

with open('./input.txt') as data:
    hash_map = {}
    for str in data.read().strip().split(','):
        match = re.match(r'([a-z]{1,})[=\-]([1-9])?', str)
        lens_label = match.group(1)
        box_num = hash_str(lens_label)
        focal_len = int(match.group(2)) if match.group(2) != None else None

        if not box_num in hash_map:
            hash_map[box_num] = OrderedDict()
        
        if focal_len:
            hash_map[box_num][lens_label] = focal_len

        else:
            if lens_label in hash_map[box_num]:
                del hash_map[box_num][lens_label]
        
    focusing_power = 0
    for box_num in range(256):
        if box_num in hash_map:
            for slot_num, focal_len in enumerate(hash_map[box_num].values()):
                focusing_power += (box_num + 1) * (slot_num + 1) * focal_len
    print(focusing_power)




        
