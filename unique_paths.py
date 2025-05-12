import copy
from fold_functions import foldl, foldr
import math

def unique_paths_leftwards(aux_info, val):
    # Using binomial numbers to get value of every point

    grid_with_vals = aux_info
    # Initialising the top of the grid with its binomial numbers
    if len(grid_with_vals) == 0:
        # Initialising the first row
        for i in range(val):
            grid_with_vals.append([i,i, math.comb(i, i), math.comb(i,i)]) # adding the temp binomial number too
        
    else:
        old_values = copy.deepcopy(grid_with_vals)
        grid_with_vals = [copy.deepcopy(old_values[-1])]

        # Making the row and column info        
        for i in range(1, val):    
            # Creating row info
            for space in old_values:
                space[0] = space[0] + 1
                
                space[2] = math.comb(space[0], space[1]) # calculating correct binomial number

            # Appending the final column data
            grid_with_vals.append(copy.deepcopy(old_values[-1]))
        
    return grid_with_vals


def unique_paths_rightwards(val, aux_info):
    # Using binomial numbers to get value of every point

    grid_with_vals = aux_info

    # Initialising the first column
    if len(grid_with_vals) == 0:
        for i in range(val):
            grid_with_vals.append([i,0, math.comb(i, 0), math.comb(i,0)])
        
    else:
        # Looping to create the final end rows and columns
        for i in range(1, val): 

            # Creating column info
            for i, space in enumerate(grid_with_vals):
                grid_with_vals[i][0] = grid_with_vals[i][0] + 1
                grid_with_vals[i][1] = grid_with_vals[i][1] + 1

                grid_with_vals[i][2] = math.comb(grid_with_vals[i][0], grid_with_vals[i][1]) # calculating correct binomial number
                # only need to store above
        
    return grid_with_vals 

# Can just say this only works for combining on the horizontal
def unique_paths_dot_operator(arr1, arr2):

    if len(arr1) != len(arr2):
        print("Cannot compute on different sizes")
        return []

    # Can change this all out for binomial math, Need to research tho
    final = []
        
    # Making sure it always goes up one as per the pattern
    val = min(arr1[0][0], arr2[0][0]) + 1
    addition_values = [val, val]

    for i in range(len(arr1)):
        num_1 = arr1[i][0] + addition_values[0]
        num_2 = arr1[i][1] + addition_values[1]
        bi_nom = math.comb(num_1, num_2)
        info = [
            num_1,
            num_2,
            bi_nom
        ]
        final.append(info)

    return final

if __name__ == '__main__':
    test_arr = [4, 5]

    # Finding the middle of the arr
    split_x = test_arr[0] // 2

    half_one  = [test_arr[0] - split_x, test_arr[1]]
    half_two  = [split_x, test_arr[1]]
    print('Info: ', half_one, half_two)

    aux_info_l = []
    aux_info_r = []

    homomorphism_left = foldl(unique_paths_leftwards, aux_info_l, half_one)

    homomorphism_right = foldr(unique_paths_rightwards, aux_info_r, half_two)

    homomorphism = unique_paths_dot_operator(homomorphism_left, homomorphism_right)

    print("Result homomorphism left:", homomorphism_left)
    print("Result homomorphism right:", homomorphism_right)

    print("Final Homomorphism: ", homomorphism)