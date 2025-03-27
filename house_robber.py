import functools
import math

def foldl(func, acc, xs):
  return functools.reduce(func, xs, acc)

def robber_left(maxs, val):

    return [maxs[1], max(maxs[0] + val, maxs[1]), maxs[3], max(maxs[2] + val, maxs[3])]


def robber_dot_operator(arr1, arr2):
    
    return max(max(arr1[0]+ arr2[1], arr1[1]+ arr2[3]),
               max(arr1[0]+ arr2[2], arr1[1] + arr2[2]),
               max(arr1[3] + arr2[3], arr1[2] + arr2[1]),
               max(arr1[3] + arr2[2], arr1[2] + arr2[0]))

if __name__ == '__main__':
    test_arr = [3,4,2,1,3,5,1]
    # test_arr = [3,4,2,1,3,5,1,4]
    # test_arr = [0,1,0,100, 1, 1, 100]
    # test_arr = [4,2,1,3,6]

    half_split_num = int(len(test_arr) / 2)
    aux_info = [0,0,-math.inf,0]

    homomorphism_left = foldl(robber_left, aux_info, test_arr[:half_split_num])
    homomorphism_right = foldl(robber_left, aux_info, test_arr[half_split_num:])
    homomorphism = robber_dot_operator(homomorphism_left, homomorphism_right)

    print("Result homomorphism left:", homomorphism_left)
    print("Result homomorphism right:", homomorphism_right)
    print("Final Homomorphism:", homomorphism)
    