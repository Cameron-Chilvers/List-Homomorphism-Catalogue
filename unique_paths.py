import copy
from fold_functions import foldl, foldr

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
    # Combine using the math
    # Do binomial math here?
    pass


test_arr = [5, 5]

# THIS SPLIT NEEDS TO BE THE NUMBER NOT THE ARR ITSELF
split_x = test_arr[0] // 2

half_one  = [test_arr[0] - split_x, test_arr[1]]
half_two  = [split_x, test_arr[1]]
print('Info: ', half_one, half_two)

aux_info = []


homomorphism_left = foldl(unique_paths_left, aux_info, half_one)

homomorphism_right = foldr(unique_paths_right, aux_info, half_two)

homomorphism = unqiue_paths_dot_operator(homomorphism_left, homomorphism_right)

print("Result homomorphism left:", homomorphism_left)
print("Result homomorphism right:", homomorphism_right)

print("Final Homomorphism: ", homomorphism)