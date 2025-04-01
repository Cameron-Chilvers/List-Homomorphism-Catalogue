from fold_functions import foldl, foldr
import math 

def mssp_left(aux_info, val):
    print("before: ", aux_info, val)

    res =  [
        max(aux_info[0] + val, val),                                               # mss[0:n]
        max(aux_info[1], aux_info[1] + val, val) if abs(aux_info[1]) - abs(aux_info[3]) != 0 else aux_info[1],        # mss including first element
        max(aux_info[0], aux_info[2]),                                         # mss including last element
        aux_info[3] + val                                                              # Sum
    ]  

    print("after: ", res)
    return res

def mssp_dot_operator_l(arr1, arr2):    
    return [
        max(arr1[0], arr2[0], (arr1[2] + arr2[1])),     # (max mssx (max mssy (mcsx + misy)),
        max(arr1[1], (arr1[3] + arr2[1])),              # max misx (tsx+misy)
        max(arr2[2], (arr1[2] + arr2[3])),              # max mcsy (mcsx+tsy)
        arr1[3] + arr2[3]                               # tsx + tsy
    ]                              



test_arr = [-1,3,4,4,-1,0]
# test_arr = [3,-4,2,1,3,5,1]
# test_arr = [2, 3, -8, 7, -1, 2, 3]

half_split_num = len(test_arr) // 2
print('Info: ',test_arr[:half_split_num], test_arr[half_split_num:])

aux_info_l = [0,-math.inf,0,0]

homomorphism_left = foldl(mssp_left, aux_info_l, test_arr[:half_split_num])
print('break')
homomorphism_left_second = foldl(mssp_left, aux_info_l, test_arr[half_split_num:])

homomorphism_l = mssp_dot_operator_l(homomorphism_left, homomorphism_left_second)

print("Result homomorphism left:", homomorphism_left)
print("Result homomorphism left second half:", homomorphism_left_second)
print("Final Homomorphism Left only:", homomorphism_l)