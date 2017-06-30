# -*- coding: utf-8 -*-
from itertools import product, combinations


def get_all_combinations(*args):
    combinations_as_tuples = product(*args)
    combinations = (list(c) for c in combinations_as_tuples)
    yield from combinations


def replace_by_x(combination, *positions):
    for position in positions:
        combination[position] = 'X'
    return ''.join(combination)

if __name__ == '__main__':
    a1 = ['E', 'I']
    a2 = ['S', 'N']
    a3 = ['T', 'F']
    a4 = ['J', 'P']
    res = []
    # Index of combinations two X in 4 positions
    # [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    comb = list(combinations(range(4), 2))

    for i, j in comb:
        combinations = get_all_combinations(a1, a2, a3, a4)
        raw_results = (replace_by_x(c, i, j) for c in combinations)
        results = sorted(list(set(raw_results)))
        res.extend(results)

    print(sorted(res))
