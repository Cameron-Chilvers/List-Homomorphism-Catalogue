import copy
from fold_functions import foldl, foldr
import math

def unique_paths_left(aux_info, val):
    # Using binomal numbers to get value of every point
    print(aux_info, val)

    grid_with_vals = aux_info
    if len(grid_with_vals) == 0:
        for i in range(val):
            grid_with_vals.append([i,i])
    else:
        grid_with_vals = [grid_with_vals]
        grid_with_vals.append([copy.deepcopy(grid_with_vals[0][-1])])

        for i in range(1, val):    
            for space in grid_with_vals[0]:
                temp = space[0] + 1
                space[0] = temp

            print(grid_with_vals[0][-1], grid_with_vals[0])
            grid_with_vals[1].append(copy.deepcopy(grid_with_vals[0][-1]))
        
    print(grid_with_vals)
    return grid_with_vals


def unique_paths_right(val, aux_info):
    pass

def unqiue_paths_dot_operator(arr1, arr2):
    # Do binomial math here?

    # [0] = Combine horizontally
    # [1] = Combine vertically

    if len(arr1[1]) != len(arr2[1]):
        print("Cannot compute on different sizes")
        return []

    # Can change this all out for binomal math, Need to research tho
    final = []
    for i in range(len(arr1[1])):
        print(i, arr1[1][i], arr2[1][-(i + 1)])
        binom_one = math.comb(arr1[1][i][0], arr1[1][i][1])
        binom_two = math.comb(arr2[1][-(i + 1)][0], arr2[1][-(i + 1)][1])
        print(binom_one, binom_two)

        if len(final) == 0:
            final.append(binom_one * binom_two)
        else: 
            final.append(final[-1]+(binom_one * binom_two))
    
    return final


test_arr = [5, 5]

# THIS SPLIT NEEDS TO BE THE NUMBER NOT THE ARR ITSELF
split_x = test_arr[0] // 2

half_one  = [test_arr[0] - split_x, test_arr[1]]
half_two  = [split_x, test_arr[1]]
print('Info: ', half_one, half_two)

aux_info = []
aux_info_2 = []


homomorphism_left = foldl(unique_paths_left, aux_info, half_one)
print("\n\n")
homomorphism_left_2 = foldl(unique_paths_left, aux_info_2, half_two)

homomorphism_right = foldr(unique_paths_right, aux_info, half_two)

print('\n\n')
homomorphism = unqiue_paths_dot_operator(homomorphism_left, homomorphism_left_2)

print("Result homomorphism left:", homomorphism_left)
print("Result homomorphism left 2:", homomorphism_left_2)
# print("Result homomorphism right:", homomorphism_right)

print("Final Homomorphism: ", homomorphism)