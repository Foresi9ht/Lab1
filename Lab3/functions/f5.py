from itertools import permutations

def string_permutations(input_str):
    return [''.join(p) for p in permutations(input_str)]