import functools
import math

def foldl(func, acc, xs):
  return functools.reduce(func, xs, acc)

# Right fold implementation using recursion as we use many elements
def foldr(func, acc, xs):
    if not xs:
        return acc
    return func(xs[0], foldr(func, acc, xs[1:]))

def robber_left(aux_info, val):
    return [
        aux_info[1],                          # max(x[0:n-1])
        max(aux_info[0] + val, aux_info[1]),  # max(x[0:n])
        aux_info[3],                          # max(x[1:n-1]) 
        max(aux_info[2] + val, aux_info[3])   # max(x[1:n])
    ]  

def robber_right(val, aux_info):
    return [
          aux_info[2],                          # max(x[1:n-1])
          aux_info[3],                          # max(x[1:n])
          max(aux_info[0] + val, aux_info[2]),  # max(x[0:n-1])
          max(aux_info[1] + val, aux_info[3])   # max(x[0:n])
      ]

def robber_dot_operator_l(arr1, arr2):    
    return max(max(arr1[0] + arr2[1], arr1[1] + arr2[3]),
               max(arr1[0] + arr2[0], arr1[1] + arr2[2]),
               max(arr1[3] + arr2[3], arr1[2] + arr2[1]),
               max(arr1[3] + arr2[2], arr1[2] + arr2[0]))

def robber_dot_operator_r(arr1, arr2):    
    return max(max(arr1[2] + arr2[3], arr1[3] + arr2[2]),
               max(arr1[2] + arr2[2], arr1[3] + arr2[0]),
               max(arr1[1] + arr2[1], arr1[0] + arr2[3]),
               max(arr1[1] + arr2[0], arr1[0] + arr2[2]))

def robber_dot_operator(arr1, arr2):    
    return max(max(arr1[0] + arr2[3], arr1[1] + arr2[1]),
               max(arr1[0] + arr2[2], arr1[1] + arr2[0]),
               max(arr1[3] + arr2[1], arr1[2] + arr2[3]),
               max(arr1[3] + arr2[0], arr1[2] + arr2[2]))

# test_arr = [3,4,2,1,3,5,1]
# test_arr = [3,4,2,1,3,5,1,4]
test_arr = [100, 1, 1, 100]
# test_arr = [4,2,1,3,6]

half_split_num = len(test_arr) // 2
print('Info: ',test_arr[:half_split_num], test_arr[half_split_num:])

aux_info_l = [0,0,-math.inf,0]
aux_info_r = [-math.inf, 0, 0, 0]

homomorphism_left = foldl(robber_left, aux_info_l, test_arr[:half_split_num])
homomorphism_left_second = foldl(robber_left, aux_info_l, test_arr[half_split_num:])


homomorphism_right = foldr(robber_right, aux_info_r, test_arr[:half_split_num])

homomorphism_right_second = foldr(robber_right, aux_info_r, test_arr[half_split_num:])

homomorphism_l = robber_dot_operator_l(homomorphism_left, homomorphism_left_second)
homomorphism_r = robber_dot_operator_r(homomorphism_right, homomorphism_right_second)

homomorphism = robber_dot_operator(homomorphism_left, homomorphism_right_second)

print("Result homomorphism left:", homomorphism_left)
print("Result homomorphism left second half:", homomorphism_left_second)
print("Final Homomorphism Left only:", homomorphism_l)

print("Result homomorphism right:", homomorphism_right)
print("Result homomorphism right second:", homomorphism_right_second)
print("Final Homomorphism right only:", homomorphism_l)

print("Final Homomorphism combine: ", homomorphism)