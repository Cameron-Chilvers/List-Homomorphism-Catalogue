from fold_functions import foldl, foldr
import re

# This only works if the automaton is in this form with the states with unique index
# Each index also refers to the order they will be placed in the aux_info
divisible_by_three = {('s0', 0): 's0', ('s0', 1): 's1',
             ('s1', 0): 's2', ('s1', 1): 's0',
             ('s2', 0): 's1', ('s2', 1): 's2'}

even_ones = {
    ('s0', 0): 's0', ('s0', 1): 's1',
    ('s1', 0): 's1', ('s1', 1): 's0'
}

# This does not work as when through the transpose function some states do not have a enter state for all language
contains_0101 =  {('s0', 0): 's1', ('s0', 1): 's0',
             ('s1', 0): 's1', ('s1', 1): 's2',
             ('s2', 0): 's3', ('s2', 1): 's0',
             ('s3', 0): 's1', ('s3', 1): 's4',
            ('s4', 0): 's4', ('s4', 1): 's4'}

# Also the same as above the transpose does not work but the leftwards function does
ends_with_0 = {
    ('s0', 0): 's1', ('s0', 1): 's2',
    ('s1', 0): 's1', ('s1', 1): 's2',
    ('s2', 0): 's1', ('s2', 1): 's2'
}

automaton = divisible_by_three
# Where s0 is the start state

# Transposed to find the right fold
# This does not deal with automatons which when transposed they are NFAs not DFAs
def transpose_automata():
    transposed_automata = {}
    for (from_state, val), to_state in automaton.items():
        if (to_state, val) not in transposed_automata:
            transposed_automata[(to_state, val)] = from_state

    return transposed_automata

# Used to create the base case
def get_unique_states():
    all_states = set()
    for state, val in automaton.keys():
        all_states.add(state)
    
    return sorted(list(all_states))

def apply_state(state, val, use_transposed = False):
    if use_transposed:
        return transpose_automata()[(state, int(val))]

    return automaton[(state, int(val))]

def automata_leftwards(aux_info, val):
    return {k: apply_state(v, val) for k, v in aux_info.items()}


def automata_rightwards(val, aux_info):
    return {k: apply_state(v, val, use_transposed=True) for k, v in aux_info.items()}


def automata_dot_operator(arr1, arr2):
    return {k: arr2[v] for k, v in arr1.items()}

def make_aux_info_dict():
    return {state: state for state in get_unique_states()}

if __name__ == '__main__':
    num = '1001'

    half_split_num = len(num) // 2
    print('Info: ',num[:half_split_num], num[half_split_num:])

    aux_info_l = make_aux_info_dict()
    aux_info_r = make_aux_info_dict()


    homomorphism_leftwards = foldl(automata_leftwards, aux_info_l, num[:half_split_num])
    homomorphism_leftwards_2 = foldr(automata_rightwards, aux_info_r, num[half_split_num:])

    print(homomorphism_leftwards)
    print(homomorphism_leftwards_2)

    homomorphism = automata_dot_operator(homomorphism_leftwards, homomorphism_leftwards_2)

    print(homomorphism)
