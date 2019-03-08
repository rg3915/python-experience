# -*- coding: utf-8 -*-

from redundancia import redun_palavra_palavra, redun_palavra_frase, redun_frase_frase


def remover_aspas(texto):
    '''
    Remove aspas, caso o texto contenha aspas no começo e no final da frase.

    Args:
       texto (str): Frase.

    Returns:
       str: Frase corrigida.
    '''
    return texto.strip('"')


def redundancia(termo, tipo, termos):
    '''
    Pega a lista de termos, verifica se tem redundancia.
    Se sim, retorna a mensagem de erro.

    Args:
        termo (str): Termo a ser analisado.
        tipo (str): Tipo, se 'A' palavra ou 'R' frase.
        termos (list): Lista de termos a serem comparados.

    Returns:
        str: Retorna a mensagem de erro.
    '''
    lista = []
    # Se o termo for uma frase 'R' de uma palavra só, então converte para palavra.
    if tipo == 'R':
        if len(remover_aspas(termo).split()) == 1:
            tipo = 'A'
            termo = remover_aspas(termo)
    if tipo == 'A':
        for i, _termo in enumerate(termos):
            meu_termo = remover_aspas(_termo['termos'])
            _tipo = _termo['tipo']
            # print(i, _termo)
            # print(i, meu_termo)
            if _tipo == 'A':
                # print('caiu no palavra palavra')
                resposta = redun_palavra_palavra(termo, meu_termo)
            else:
                # print('caiu no palavra frase')
                resposta = redun_palavra_frase(termo, meu_termo)
            # print(i, 'antes', resposta)
            if resposta:
                lista.append(resposta)
            # print(i, 'depois', resposta)
    else:
        # Se tipo for igual a 'R', considerando a query.
        for _termo in termos:
            meu_termo = remover_aspas(_termo['termos'])
            _tipo = _termo['tipo']
            if _tipo == 'R':
                resposta = redun_frase_frase(remover_aspas(termo), meu_termo)
            else:
                # Se for 'A', então troca palavra e frase de lugar
                # pra usar a mesma função.
                tmp_palavra = meu_termo
                tmp_frase = remover_aspas(termo)
                resposta = redun_palavra_frase(tmp_palavra, tmp_frase)
            if resposta:
                lista.append(resposta)
    print('\n')
    print('lista')
    print(lista)
    if lista:
        msg_error = "O termo '%s' é redundante." % lista[0]['quem']
        return msg_error
    return

termos = (
    # {'termos': 'Ciro', 'id': 20, 'tipo': 'A'},
    # {'termos': 'Ciro Gomes', 'id': 20, 'tipo': 'A'},
    # {'termos': '"Ciro Gomes Silva Augusto"', 'id': 21, 'tipo': 'R'},
    # {'termos': 'Gomes', 'id': 22, 'tipo': 'A'},
    # {'termos': 'Silva', 'id': 23, 'tipo': 'A'},
    # {'termos': 'Augusto', 'id': 24, 'tipo': 'A'},
    # {'termos': '"Antonio Santos"', 'id': 25, 'tipo': 'R'},
    # {'termos': 'Antonio', 'id': 26, 'tipo': 'A'},
    # {'termos': '"Antonio"', 'id': 27, 'tipo': 'R'},
    # {'termos': 'americanas', 'id': 28, 'tipo': 'A'}, # OK
    # {'termos': '"americanas teste"', 'id': 29, 'tipo': 'R'}, # OK
    # #
    # OK {'termos': 'submarino amarelo', 'id': 30, 'tipo': 'A'},
    # OK {'termos': '"submarino amarelo"', 'id': 31, 'tipo': 'R'},
    # OK {'termos': '"submarino amarelo"', 'id': 32, 'tipo': 'R'},
    {'termos': 'submarino amarelo', 'id': 33, 'tipo': 'A'},
    # OK {'termos': 'submarino verde amarelo', 'id': 34, 'tipo': 'A'},
    # OK {'termos': '"submarino verde amarelo"', 'id': 35, 'tipo': 'R'},
)


# res = redundancia('Ciro', 'A', termos)
# print(res)

# res = redundancia('Antonio', 'R', termos)
# print(res)

# res = redundancia('Pedro', 'A', termos)
# print(res)

# res = redundancia('aaa', 'A', termos)
# print(res)

# res = redundancia('americanas', 'A', termos)  # OK
# print(res)

# res = redundancia('"americanas teste"', 'R', termos)
# print(res)

# # 1 OK
# res = redundancia('submarino', 'A', termos)
# print(res)

# # 2 OK
# res = redundancia('"submarino"', 'R', termos)
# print('2 - %s' % res)

# # 3 OK
# res = redundancia('submarino', 'A', termos)
# print('3 - %s' % res)

# # 4 REVER
res = redundancia('"submarino"', 'R', termos)
print('4 - %s' % res)

# # 5 OK
# res = redundancia('"submarino verde"', 'R', termos)
# print('5 - %s' % res)

# # 6 Ok
# res = redundancia('submarino verde', 'A', termos)
# print('6 - %s' % res)
