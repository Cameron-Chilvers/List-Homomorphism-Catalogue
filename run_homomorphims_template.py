import time
from concurrent.futures import ThreadPoolExecutor

from house_robber import robber_dot_operator
from best_time_to_buy import best_time_dot_operator
from mssp import mssp_dot_operator
from automata import apply_state, automata_dot_operator, make_aux_info_dict
from unique_paths import unique_paths_dot_operator

test_arr_best = [7,1,5,3,6,4]
test_arr_rob = [1,5,3,2,4,3]
test_arr_mssp = [2, 3, -8, 7, -1, 2, 3]
test_automata = '1001'
test_unique = [5, 5, 5]

def return_robber_base(val):
    return [0,val, 0, 0]

def return_best_base(val):
    return [val, val, 0]

def return_mssp_base(val):
    return [val] * 4

def return_automata_base(val):
    return {k: apply_state(v, val) for k, v in make_aux_info_dict().items()}

def return_unique_base(val):
    base = []
    for i in range(val):
        base.append([
            i,
            0,
            1
        ])
    return base

def bottom_up(arr, base_function, dot_operator):
    base_arr = [base_function(val) for val in arr]

    start_time = time.perf_counter()
    while len(base_arr) > 1:
        temp_arr = []

        for i in range(0, len(base_arr)-1, 2):
            temp_arr.append(dot_operator(base_arr[i], base_arr[i+1]))

        if len(base_arr) % 2 == 1:
            temp_arr.append(base_arr[-1])

        base_arr = temp_arr
    end_time = time.perf_counter()
    duration = end_time - start_time
    return base_arr[0], duration

def bottom_up_parallel(arr, base_function, dot_operator, max_workers=None):
    base_arr = [base_function(val) for val in arr]

    start_time = time.perf_counter()

    while len(base_arr) > 1:
        temp_arr = []
        tasks = []

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            for i in range(0, len(base_arr) - 1, 2):
                tasks.append(executor.submit(dot_operator, base_arr[i], base_arr[i+1]))

            for future in tasks:
                temp_arr.append(future.result())

        if len(base_arr) % 2 == 1:
            temp_arr.append(base_arr[-1])

        base_arr = temp_arr

    end_time = time.perf_counter()
    duration = end_time - start_time
    return base_arr[0], duration

def run_all_functions(arr, base_function, dot_operator):
    return bottom_up(arr, base_function, dot_operator)

def run_all_functions_parallel(arr, base_function, dot_operator):
    return bottom_up_parallel(arr, base_function, dot_operator)

# Run and print both serial and parallel versions
for name, arr, base_fn, dot_op in [
    ("Best time to buy", test_arr_best, return_best_base, best_time_dot_operator),
    ("House Robber", test_arr_rob, return_robber_base, robber_dot_operator),
    ("MSSP", test_arr_mssp, return_mssp_base, mssp_dot_operator),
    ("Automata", test_automata, return_automata_base, automata_dot_operator),
    ("Unique Paths", test_unique, return_unique_base, unique_paths_dot_operator),
]:
    result_seq, time_seq = run_all_functions(arr, base_fn, dot_op)
    result_par, time_par = run_all_functions_parallel(arr, base_fn, dot_op)
    print(f"{name} Sequential: {result_seq}, Time: {time_seq:.6f}s")
    print(f"{name} Parallel:   {result_par}, Time: {time_par:.6f}s\n")