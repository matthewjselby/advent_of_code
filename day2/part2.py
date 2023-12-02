import re

def get_cube_power(line):
    # get min number of red cubes
    min_red_cubes = 0
    red_cube_regex = re.compile(r'([0-9]{1,3})(?: red)')
    for num_red_cubes_text in red_cube_regex.findall(line):
        num_red_cubes = int(num_red_cubes_text)
        if num_red_cubes > min_red_cubes:
            min_red_cubes = num_red_cubes
    # get min number of green cubes
    min_green_cubes = 0
    green_cube_regex = re.compile(r'([0-9]{1,3})(?: green)')
    for num_green_cubes_text in green_cube_regex.findall(line):
        num_green_cubes = int(num_green_cubes_text)
        if num_green_cubes > min_green_cubes:
            min_green_cubes = num_green_cubes
    # get min number of blue cubes
    min_blue_cubes = 0
    blue_cube_regex = re.compile(r'([0-9]{1,3})(?: blue)')
    for num_blue_cubes_text in blue_cube_regex.findall(line):
        num_blue_cubes = int(num_blue_cubes_text)
        if num_blue_cubes > min_blue_cubes:
            min_blue_cubes = num_blue_cubes
    return min_red_cubes * min_green_cubes * min_blue_cubes

with open('./input.txt') as input:
    lines = input.readlines()
    cube_power_sum = 0
    for line in lines:
        cube_power_sum += get_cube_power(line)
    print(cube_power_sum)