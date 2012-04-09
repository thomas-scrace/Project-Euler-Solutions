'''
Euler problem 11.
Thomas Scrace
March 2011
'''
FILE_NAME = '11rawdata.txt'

def build_grid(file_name):
    grid = {}
    row_ctr = 0
    col_ctr = 0
    number = ''
    f = open(file_name)
    for line in f:
        col_ctr = 0
        row_ctr += 1
        for char in line:
            if char in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                number += char
            else:
                col_ctr += 1
                grid[(col_ctr, row_ctr)] = int(number)
                number = ''
    return grid

def groups_with_number(base, grid):
    for direction in ['u', 'ur', 'r', 'dr', 'd', 'dl', 'l', 'ul']:
        g = get_group(base, direction, grid[base], 0, grid)

def get_group(base, direction, product, ctr, grid):
    if ctr == 3:
        answers.append(product)
        return
    r = number_in_direction(base, direction, grid)
    if r[0] != 'N':
        get_group(r[1], direction, product * r[0], ctr + 1, grid)
    else:
        return 0

def number_in_direction(base, direction, grid):
    if direction == 'u':
        return [grid.get((base[0], base[1]-1), 'N'), (base[0], base[1]-1)]
    elif direction == 'ur':
        return [grid.get((base[0]+1, base[1]-1), 'N'), (base[0]+1, base[1]-1)]
    elif direction == 'r':
        return [grid.get((base[0]+1, base[1]), 'N'), (base[0]+1, base[1])]
    elif direction == 'dr':
        return [grid.get((base[0]+1, base[1]+1), 'N'), (base[0]+1, base[1]+1)]
    elif direction == 'd':
        return [grid.get((base[0], base[1]+1), 'N'), (base[0], base[1]+1)]
    elif direction == 'dl':
        return [grid.get((base[0]-1, base[1]+1), 'N'), (base[0]-1, base[1]+1)]
    elif direction == 'l':
        return [grid.get((base[0]-1, base[1]), 'N'), (base[0]-1, base[1])]
    elif direction == 'ul':
        return [grid.get((base[0]-1, base[1]-1), 'N'), (base[0]-1, base[1]-1)]

def get_all_groups(grid):
    for key in grid.keys():
        groups_with_number(key, grid)

answers = []
get_all_groups(build_grid(FILE_NAME))
print max(answers)







