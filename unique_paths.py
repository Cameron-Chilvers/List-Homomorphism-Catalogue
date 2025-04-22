import copy
from fold_functions import foldl, foldr
import math

def unique_paths_leftwards(aux_info, val):
    # Using binomal numbers to get value of every point

    grid_with_vals = aux_info
    # Initialising the top of the grid with its binomial numbres
    if len(grid_with_vals) == 0:
        # Intitalising the first row
        for i in range(val):
            grid_with_vals.append([i,i])

        # Creating final data structure
        grid_with_vals = [grid_with_vals]
        grid_with_vals.append([copy.deepcopy(grid_with_vals[0][-1])])
    else:
        # Making the row and column info        
        for i in range(1, val):    
            # Creating row info
            for space in grid_with_vals[0]:
                space[0] = space[0] + 1

            # Appending the final column data
            grid_with_vals[1].append(copy.deepcopy(grid_with_vals[0][-1]))
        
    return grid_with_vals


def unique_paths_rightwards(val, aux_info):
    # Using binomal numbers to get value of every point

    grid_with_vals = aux_info
    # Intitalising the first column
    if len(grid_with_vals) == 0:
        for i in range(val):
            grid_with_vals.append([i,0])

        # Build final data structure 
        grid_with_vals = [grid_with_vals]
        grid_with_vals.append([copy.deepcopy(grid_with_vals[0][-1])])

        # Reverse array as the rightwards does it in the opposite direction
        grid_with_vals = grid_with_vals[::-1]
    else:
        # Looping to create the final end rows and columns
        for i in range(1, val): 
            # Creating column info
            for space in grid_with_vals[1]:
                space[0] = space[0] + 1
                space[1] = space[1] + 1

            # Appending the final row data
            grid_with_vals[0].append(copy.deepcopy(grid_with_vals[1][-1]))
        
    return grid_with_vals 

def unqiue_paths_dot_operator(arr1, arr2):
    # [0] = Combine vertically
    # [1] = Combine horizontally

    if len(arr1[1]) != len(arr2[1]):
        print("Cannot compute on different sizes")
        return []

    # Can change this all out for binomal math, Need to research tho
    final = []
    for i in range(len(arr1[1])):
        binom_one = math.comb(arr1[1][i][0], arr1[1][i][1])
        binom_two = math.comb(arr2[1][-(i + 1)][0], arr2[1][-(i + 1)][1])

        if len(final) == 0:
            final.append(binom_one * binom_two)
        else: 
            final.append(final[-1]+(binom_one * binom_two))
    
    return final


test_arr = [2, 6]

# Finding the middle of the arr
split_x = test_arr[0] // 2

half_one  = [test_arr[0] - split_x, test_arr[1]]
half_two  = [split_x, test_arr[1]]
print('Info: ', half_one, half_two)

aux_info_l = []
aux_info_r = []

homomorphism_left = foldl(unique_paths_leftwards, aux_info_l, half_one)

homomorphism_right = foldr(unique_paths_rightwards, aux_info_r, half_two)

homomorphism = unqiue_paths_dot_operator(homomorphism_left, homomorphism_right)

print("Result homomorphism left:", homomorphism_left)
print("Result homomorphism right:", homomorphism_right)

print("Final Homomorphism: ", homomorphism)