import math
from fold_functions import foldl, foldr

def best_time_leftwards(aux_info, val):
    return [
            min(aux_info[0], val),
            max(aux_info[1], val),
            max(aux_info[2], val - min(aux_info[0], val))
        ]


def best_time_rightwards(val, aux_info):
    return [
            min(aux_info[0], val),
            max(aux_info[1], val),
            max(aux_info[2], max(aux_info[1], val) - val)
        ]

# Fix dot operators
def best_time_dot_operator(arr1, arr2):
    return [
        min(arr1[0], arr2[0]), 
        max(arr1[1], arr2[1]), 
        max(arr1[2], arr2[2], arr2[1] - arr1[0] if arr2[1] - arr1[0] > 0 else 0)
    ]

if __name__ == '__main___':
    test_arr = [7,1,5,3,6,4]
    # test_arr = [7,6,4,3,1]

    aux_info_l = [math.inf,-math.inf,-math.inf]
    aux_info_r = [math.inf,-math.inf,-math.inf]

    split_num = len(test_arr) // 2

    homomorphism_leftwards = foldl(best_time_leftwards, aux_info_l, test_arr[:split_num])
    homomorphism_rightwards = foldr(best_time_rightwards, aux_info_r, test_arr[split_num:])

    print("FINAL", homomorphism_leftwards)
    print("FINAL2", homomorphism_rightwards)

    homomorphism = best_time_dot_operator(homomorphism_leftwards, homomorphism_rightwards)

    print("FINAL FINAL", homomorphism)