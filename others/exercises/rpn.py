# Notação polonesa reversa

'''
>>>
40 2 +
42
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


if __name__ == '__main__':
    print(rpn())
