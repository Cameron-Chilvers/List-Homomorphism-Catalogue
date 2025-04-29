from fold_functions import foldl, foldr
import math 

def mssp_leftwards(aux_info, val):
    # Written for ease of use
    sum = aux_info[3] + val 
    
    return [
        max(aux_info[0], aux_info[2] + val, val),     # mss[0:n]
        max(sum, aux_info[1]),                        # mss including first element (mfe)
        max(aux_info[2] + val, val),                  # mss including last element (mle)
        sum                                           # Sum
    ]  

def mssp_rightwards(val, aux_info):
    # Written for ease of use
    sum = aux_info[3] + val

    return [
        max(aux_info[0], aux_info[1] + val, val),     # mss[0:n]
        max(aux_info[1] + val, val),                  # mss including first element (mfe)
        max(sum, aux_info[2]),                        # mss including last element (mle)
        sum                                           # Sum
    ]  


def mssp_dot_operator(arr1, arr2):    
    return [
        max(arr1[0], arr2[0], arr1[2] + arr2[1]),     # max(mssx, mssy, mlex + mfey)
        max(arr1[1], arr1[3] + arr2[1]),              # max(mfex, tsx + mfey)
        max(arr2[2], arr1[2] + arr2[3]),              # max(mley, mlex + tsy)
        arr1[3] + arr2[3]                             # tsx + tsy
    ]                              


if __name__ == "__main__":
    # test_arr = [-1,3,4,4,-1,-1]
    # test_arr = [3,-4,2,1,3,5,1]
    test_arr = [2, 3, -8, 7, -1, 2, 3]

    half_split_num = len(test_arr) // 2
    print('Info: ',test_arr[:half_split_num], test_arr[half_split_num:])

    print(mssp_leftwards([-math.inf,-math.inf,-math.inf,0], 3))


    aux_info_l = [-math.inf,-math.inf,-math.inf,0]
    aux_info_r = [-math.inf,-math.inf,-math.inf,0]

    homomorphism_left = foldl(mssp_leftwards, aux_info_l, test_arr[:half_split_num])

    homomorphism_right = foldr(mssp_rightwards, aux_info_r, test_arr[half_split_num:])

    homomorphism = mssp_dot_operator(homomorphism_left, homomorphism_right)

    print("Result homomorphism left:", homomorphism_left)
    print("Result homomorphism right:", homomorphism_right)
    print("Final Homomorphism:", homomorphism)