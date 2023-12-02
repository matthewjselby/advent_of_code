import re

def check_cubes(line):
    # get game number
    game_number_regex = re.compile(r'Game ([0-9]{1,3})')
    game_number = int(game_number_regex.search(line).group(1))
    # check number of red cubes
    red_cube_regex = re.compile(r'([0-9]{1,3})(?: red)')
    for num_red_cubes in red_cube_regex.findall(line):
        if int(num_red_cubes) > 12:
            return 0
    # check number of green cubes
    green_cube_regex = re.compile(r'([0-9]{1,3})(?: green)')
    for num_green_cubes in green_cube_regex.findall(line):
        if int(num_green_cubes) > 13:
            return 0
    # check number of blue cubes
    blue_cube_regex = re.compile(r'([0-9]{1,3})(?: blue)')
    for num_blue_cubes in blue_cube_regex.findall(line):
        if int(num_blue_cubes) > 14:
            return 0
    return game_number

with open('./input.txt') as input:
    lines = input.readlines()
    possible_games_sum = 0
    for line in lines:
        possible_games_sum += check_cubes(line)
    print(possible_games_sum)
