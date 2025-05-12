import math
from fold_functions import foldl, foldr

def robber_leftwards(aux_info, val):
    return [
        aux_info[1],                            # max(x[0:n-1])
        max(aux_info[0] + val, aux_info[1]),    # max(x[0:n])
        aux_info[3],                            # max(x[1:n-1]) 
        max(aux_info[2] + val, aux_info[3])     # max(x[1:n])
    ]  

def robber_rightwards(val, aux_info):
    return [
          max(aux_info[2] + val, aux_info[0]),  # max(x[0:n-1])
          max(aux_info[3] + val, aux_info[1]),  # max(x[0:n])
          aux_info[0],                          # max(x[1:n-1]) 
          aux_info[1]                           # max(x[1:n])
      ]

def robber_dot_operator(arr1, arr2):    
    return [max(arr1[0] + arr2[0], arr1[1] + arr2[2]), 
            max(arr1[0] + arr2[1], arr1[1] + arr2[3]), 
            max(arr1[2] + arr2[0], arr1[3] + arr2[2]), 
            max(arr1[2] + arr2[1], arr1[2] + arr2[3])]   

if __name__ == '__main__':
    # test_arr = [3,4,2,1,3,5,1]
    test_arr = [3,4,2,1,3,5,1,4]
    # test_arr = [100, 1, 1, 100]
    # test_arr = [4,2,1,3,6]
    test_arr = [1,5,3,2,4,3]

    half_split_num = len(test_arr) // 2
    print('Info: ',test_arr[:half_split_num], test_arr[half_split_num:])

    aux_info_l = [0,0,-math.inf,0]
    aux_info_r = [0,0,-math.inf,0]

    print(robber_leftwards([0,0,-math.inf,0], 3))

    homomorphism_left = foldl(robber_leftwards, aux_info_l, test_arr[:half_split_num])

    homomorphism_right = foldr(robber_rightwards, aux_info_r, test_arr[half_split_num:])

    homomorphism = robber_dot_operator(homomorphism_left, homomorphism_right)

    print("Result homomorphism left:", homomorphism_left)
    print("Result homomorphism right:", homomorphism_right)

    print("Final Homomorphism: ", homomorphism)