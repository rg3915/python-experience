#-*- coding: utf-8 -*-

from unittest.mock import patch


# Notação polonesa reversa


'''
>>>
40 2 +
42
>>>
40 2 -
38
>>>
40 2 *
80
>>>
40 2 //
20
>>>
40 2 /
20
>>>
40 2 %
0
'''


def rpn():
    a, b, sinal = input().split()
    a, b = int(a), int(b)
    switch = {
        '+': '__add__',
        '-': '__sub__',
        '*': '__mul__',
        '//': '__floordiv__',
        '/': '__div__',
        '%': '__mod__',
        '**': '__pow__'
    }
    dunder_method = switch.get(sinal)
    return getattr(a, dunder_method)(b)

def is_float(num):
    return '.' in num

def rpn(expr):
    if not expr:
        return 0
    expr = expr.split(' ')
    stack = []
    for n in expr:
        if n.isdigit() or is_float(n):
            stack.append(n)
        else:
            num = str(eval('{2}{1}{0}'.format(stack.pop(), n, stack.pop())))
            stack.append(num)
    return float(stack[-1]) if '.' in stack[-1] else int(stack[-1])


def test_rpn():
    with patch('__main__.input') as mocked_input:
        mocked_input.return_value = '40 2 +'
        assert rpn() == 42


if __name__ == '__main__':
    print(rpn('5 1 2 + 4 * + 3 -'))
    print(rpn(''))
    print(rpn('1 2 3'))
    print(rpn('1 3 +'))
    print(rpn('1 3 *'))
    print(rpn('1 3 -'))
    print(rpn('4 2 /'))
    print(rpn('1 3 5 +'))
    print(rpn('10 3 2 -'))
