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
            grid_with_vals.append([i,i, math.comb(i, i)]) # adding the temp binomal number too

        # Creating final data structure
        grid_with_vals = [grid_with_vals]
        grid_with_vals.append([copy.deepcopy(grid_with_vals[0][-1])])
        
        print("FIRST grif with vals", grid_with_vals)
    else:
        # Making the row and column info        
        for i in range(1, val):    
            # Creating row info
            for space in grid_with_vals[0]:
                space[0] = space[0] + 1
                
                space[2] = math.comb(space[0], space[1]) # calculating correct binomial number

            # Appending the final column data
            grid_with_vals[1].append(copy.deepcopy(grid_with_vals[0][-1]))
        
    return grid_with_vals


def unique_paths_rightwards(val, aux_info):
    # Using binomal numbers to get value of every point

    grid_with_vals = aux_info
    # Intitalising the first column
    if len(grid_with_vals) == 0:
        for i in range(val):
            grid_with_vals.append([i,0, math.comb(i, 0)])

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

                space[2] = math.comb(space[0], space[1]) # calculating correct binomial number
                print(space)

            # Appending the final row data
            grid_with_vals[0].append(copy.deepcopy(grid_with_vals[1][-1]))
            print(grid_with_vals)
        
    return grid_with_vals 

# Why not just do the leftwards and rightwrd logic here, oh wait cause need to resutn list ....
# cannot jsut pass up nuimerb
def unqiue_paths_dot_operator_horizontal(arr1, arr2):
    # [1] = Combine horizontally
    if len(arr1) != len(arr2):
        print("Cannot compute on different sizes")
        return []

    # Can change this all out for binomal math, Need to research tho
    final = []
    for i in range(len(arr1)):
        # Adding for storage
        final.append([])

        if i == 0 or i == 1:
            # Extend
            final[i].extend(arr1[i])

            print(final)
            for j in range(len(arr2[i])):
                
                info = [
                    arr1[i][-1][0] + j + 1,
                    arr1[i][-1][1] + j + 1,
                    math.comb(arr1[i][-1][0] + j + 1, arr1[i][-1][1] + j + 1)
                ]

                final[i].append(info)
                print("J", j)

        else:
            # FIND THE COMBINATION OF THE TWO ROWS
            for j in range(len(arr1[i])):
                if len(final[i]) == 0:
                    final[i].append(['temp', 'temp', arr1[i][j][2] * arr2[i][-(j+1)][2]])
                else: 
                    final[i].append(['temp', 'temp', final[i][-1][-1]+(arr1[i][j][2] * arr2[i][-(j+1)][2])])

    return final

if __name__ == '__main__':
    test_arr = [5, 5]

    # Finding the middle of the arr
    split_x = test_arr[0] // 2

    half_one  = [test_arr[0] - split_x, test_arr[1]]
    half_two  = [split_x, test_arr[1]]
    print('Info: ', half_one, half_two)

    aux_info_l = []
    aux_info_r = []

    print('Leftwards \n\n')
    homomorphism_left = foldl(unique_paths_leftwards, aux_info_l, half_one)

    print('Rightwards \n\n')

    homomorphism_right = foldr(unique_paths_rightwards, aux_info_r, half_two)

    homomorphism = unqiue_paths_dot_operator_horizontal(homomorphism_left, homomorphism_right)

    print("Result homomorphism left:", homomorphism_left)
    print("Result homomorphism right:", homomorphism_right)

    print("Final Homomorphism: ", homomorphism)