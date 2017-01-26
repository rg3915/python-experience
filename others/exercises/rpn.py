# Notação polonesa reversa

'''
>>>
40 2 +
42
'''


def obter_input():
    valor = input()
    d = {}
    d['a'] = valor.split()[0]
    d['b'] = valor.split()[1]
    d['sinal'] = valor.split()[2]
    return d


def soma(a, b, sinal):
    return a + b


def rpn():
    res = obter_input()
    a = int(res['a'])
    b = int(res['b'])
    sinal = res['sinal']
    return soma(a, b, sinal)


if __name__ == '__main__':
    print(rpn())
