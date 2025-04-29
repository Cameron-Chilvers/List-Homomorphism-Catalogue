from house_robber import robber_dot_operator
from best_time_to_buy import best_time_dot_operator
from mssp import mssp_dot_operator

test_arr_best = [7,1,5,3,6,4]
test_arr_rob = [1,5,3,2,4,3]
test_arr_mssp = [2, 3, -8, 7, -1, 2, 3]

def return_robber_base(val):
    return [0,val, 0, 0]

def return_best_base(val):
    return [val, val, 0]

def return_mssp_base(val):
    return [val] * 4

def run_all_function(arr, base_function, dot_operator):
    base_arr = [base_function(val) for val in arr]

    while len(base_arr) > 1:
        temp_arr = []

        for i in range(0, len(base_arr)-1, 2):
            temp_arr.append(dot_operator(base_arr[i], base_arr[i+1]))

        if len(base_arr) % 2 == 1:
            temp_arr.append(base_arr[-1])
            
        base_arr = temp_arr

    return base_arr[0]

print("Best time to buy:", run_all_function(test_arr_best, return_best_base, best_time_dot_operator))
print("House Robber:", run_all_function(test_arr_rob, return_robber_base, robber_dot_operator))
print("Mssp:", run_all_function(test_arr_mssp, return_mssp_base, mssp_dot_operator))

