# troyjlee@gmail.com


import functools
import operator

def foldl(func, acc, xs):
  return functools.reduce(func, xs, acc)

def robber_left(maxs, val):
    return [maxs[1], max(maxs[0] + val, maxs[1])]

# tests
print(foldl(robber_left, [0,0], [100,1,1,100])) # -6
print(foldl(operator.add, 'L', ['1','2','3'])) # 'L123'


def robber_leftwards(arr):

    if len(arr) <= 0:
        raise Exception("Need at least length 1")
    
    # Creating maximumn list of zero
    maximums = [0] * len(arr)

    # First value has to be the max
    maximums[0] = arr[0]
    total_max = arr[0]

    # Second value max is either the first value or itself
    if len(arr) > 1:    
        maximums[1] = max(arr[0], arr[1])

    # Maximum of the current values is the max of the previous value
    # Or the maximum two houses ago plus the current value
    for i in range(2, len(arr)):
        maximums[i] = max(maximums[i-1], maximums[i-2] + arr[i])
        
        # Tracking total max
        if maximums[i] > total_max:
            total_max = maximums[i]

    return total_max

def robber_rightwards(arr):
    if len(arr) <= 0:
        raise Exception("Need at least length 1")
    
    # Creating maximumn list of zero
    maximums = [0] * len(arr)

    # Last value has to be the max
    maximums[-1] = arr[-1]
    total_max = arr[-1]

    # Second last value max is either the last value or itself
    if len(arr) > 1:    
        maximums[-2] = max(arr[-1], arr[-2])

    # Maximum of the current values is the max of the previous value
    # Or the maximum two houses forward plus the current value
    for i in range(len(arr)-3, -1, -1):
        maximums[i] = max(maximums[i+1], maximums[i+2] + arr[i])
        
        # Tracking total max
        if maximums[i] > total_max:
            total_max = maximums[i]

    return total_max

def robber_homomorphism_worker(arr):
    if len(arr) <= 0:
        raise Exception("Need at least length 1")

    if len(arr) > 1:
        aux_value_1 = robber_leftwards(arr)
        aux_value_2 = robber_leftwards(arr[:-1])
        aux_value_3 = robber_leftwards(arr[1:])
        aux_value_4 = robber_leftwards(arr[1:-1])
    else:
        # Length has to equal one
        aux_value_1 = arr[0]
        aux_value_2 = arr[0]
        aux_value_3 = arr[0]
        aux_value_4 = arr[0]

    return [aux_value_1, aux_value_2, aux_value_3, aux_value_4]

def robber_dot_operator(arr1, arr2):
    
    return max(max(arr1[1]+ arr2[0], arr1[0]+ arr2[2]),
               max(arr1[1]+ arr2[1], arr1[0] + arr2[3]),
               max(arr1[2] + arr2[2], arr1[3] + arr2[0]),
               max(arr1[2] + arr2[3], arr1[3] + arr2[1]))

if __name__ == '__main__':
    # test_arr = [3,4,2,1,3,5,1]
    # test_arr = [3,4,2,1,3,5,1,4]
    test_arr = [100, 1, 1, 100]

    print(test_arr[:3], test_arr[3:])

    leftwards = robber_leftwards(test_arr)
    rightwards = robber_rightwards(test_arr)

    homomorphism_left = robber_homomorphism_worker(test_arr[0:3])
    homomorphism_right = robber_homomorphism_worker(test_arr[3:])
    homomorphism = robber_dot_operator(homomorphism_left, homomorphism_right)

    print("Result left:", leftwards)
    print("Result right:", rightwards)

    print("Result homomorphism left:", homomorphism_left)
    print("Result homomorphism right:", homomorphism_right)
    print("Final Homomorphism:", homomorphism)
    