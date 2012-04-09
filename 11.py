'''
Euler problem 11.

Thomas Scrace
March 2011

This determines the greatest product of four adjacent (up, down, right, left, diagonal) numbers in a 20x20 grid.

First, we build the grid from a .txt file into dicionary of coord keys against number values.

For all numbers in the grid, get all the possible groups of 4 that we haven't seen before that include that number.

Finally, we just return the group with the highest product.

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
    #groups = []
    for direction in ['u', 'ur', 'r', 'dr', 'd', 'dl', 'l', 'ul']:
        g = get_group(base, direction, grid[base], 0, grid)
        #groups.append(g)
    #return groups

def get_group(base, direction, product, ctr, grid):
    if ctr == 3:
        answers.append(product)
        return #product
    r = number_in_direction(base, direction, grid)
    if r[0] != 'N':
        get_group(r[1], direction, product * r[0], ctr + 1, grid)
    else:
        return 0

def number_in_direction(base, direction, grid):
    '''Returns a list whose first element will be the value of the number
    in the given direction, and whose second element will be the key to
    that value. If no key exists, 'N', is returned. '''
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
    #groups = []
    for key in grid.keys():
        #for group in groups_with_number(key, grid):
        groups_with_number(key, grid)
            #groups.append(group)
    #return groups

#def find_answer(grid):
    #return max(get_all_groups(grid))

answers = []
#print find_answer(build_grid(FILE_NAME))
get_all_groups(build_grid(FILE_NAME))
print max(answers)







