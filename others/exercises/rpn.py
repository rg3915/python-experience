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


def test_rpn():
    with patch('__main__.input') as mocked_input:
        mocked_input.return_value = '40 2 +'
        assert rpn() == 42


if __name__ == '__main__':
    print(rpn())
