# -*- coding: utf-8 -*-
from itertools import product


def get_all_combinations(*args):
    combinations_as_tuples = product(*args)
    combinations = (list(c) for c in combinations_as_tuples)
    yield from combinations


def replace_by_x(pos, combination):
    combination[pos] = 'X'
    return ''.join(combination)


if __name__ == '__main__':
    a1 = ['E', 'I']
    a2 = ['S', 'N']
    a3 = ['T', 'F']
    a4 = ['J', 'P']

    for position in range(4):
        combinations = get_all_combinations(a1, a2, a3, a4)
        raw_results = (replace_by_x(position, c) for c in combinations)
        results = sorted(list(set(raw_results)))
        print(results)
