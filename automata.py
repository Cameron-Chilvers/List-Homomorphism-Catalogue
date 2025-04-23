from fold_functions import foldl, foldr

# This only works if the automaton is in this form with the states with unique index
# Each index also refers to the order they will be placed in the aux_info
automaton = {('s0', 0): 's0', ('s0', 1): 's1',
             ('s1', 0): 's2', ('s1', 1): 's0',
             ('s2', 0): 's1', ('s2', 1): 's2'}
# Where s0 is the start state

# need to make a reverse function for automatons
# transpose

def apply_state(state,val):
    return automaton[(state, int(val))]

def automata_leftwards(aux_info, val):
    final = []
    for i in range(len(aux_info)):
        final.append(apply_state(aux_info[i], int(val)))

    return final

def automata_rightwards(val, aux_info):
    return

def automata_dot_operator(arr1, arr2):
    final = []

    for i in range(len(arr1)):
        final.append(arr2[int(arr1[i][-1])])

    return final

num = '110101001'

half_split_num = len(num) // 2
print('Info: ',num[:half_split_num], num[half_split_num:])

aux_info_l = ['s0','s1','s2']
aux_info_r = ['s0','s1','s2']


homomorphism_leftwards = foldl(automata_leftwards, aux_info_l, num[:half_split_num])
homomorphism_leftwards_2 = foldl(automata_leftwards, aux_info_l, num[half_split_num:])

print(homomorphism_leftwards)
print(homomorphism_leftwards_2)

homomorphism = automata_dot_operator(homomorphism_leftwards, homomorphism_leftwards_2)

print(homomorphism)

curr_state = 's0'
for char in num:
    curr_state = apply_state(curr_state, char)

print(curr_state == 's0')

