# -*- coding: utf-8 -*-

'''
Procura por redundancia entre:

* Palavra e Palavra
* Frase e Frase
* Palavra e Frase

Rodar:

# python -m doctest redundancia.py -v
# python test_redundancia.py -v

>>> redun_palavra_palavra(u'João', u'João Augusto')
{'eh_redundante': True, 'quem': u'João Augusto'}

>>> redun_palavra_palavra(u'João Augusto', u'João Augusto Pereira')
{'eh_redundante': True, 'quem': u'João Augusto Pereira'}

# >>> redun_palavra_palavra(u'João Augusto', u'João Pereira Augusto')
'eh_redundante': True, 'quem': u'João Pereira Augusto'}

# >>> redun_palavra_palavra(u'João Augusto', u'João Pereira')
# False
u'João Pereira'

# >>> redun_palavra_palavra(u'João Maria', u'Maria João')
'eh_redundante': True, 'quem': u'Maria João'}

# >>> redun_palavra_palavra(u'Maria João', u'João Maria')
'eh_redundante': True, 'quem': u'João Maria'}

# >>> redun_palavra_palavra(u'Maria João Silva', u'João Maria')
'eh_redundante': True, 'quem': u'João Maria'}

# >>> redun_palavra_palavra(u'José Augusto', u'José Silva')
{}

# >>> redun_palavra_palavra(u'José Augusto', u'João Augusto')
{}

# >>> redun_palavra_palavra(u'João Silva', u'José Silva')
{}

# >>> redun_palavra_palavra(u'João Silva', u'João Augusto')
{}

# >>> redun_palavra_palavra(u'José Silva', u'João Augusto')
{}

# >>> redun_palavra_palavra(u'José Fernandes', u'José Fernandes Silva')
'eh_redundante': True, 'quem': u'José Fernandes Silva'}

# >>> redun_palavra_palavra(u'José Fernandes', u'José Silva Fernandes')
'eh_redundante': True, 'quem': u'José Silva Fernandes'}

# >>> redun_palavra_palavra(u'José Fernandes Silva', u'José Silva Fernandes')
'eh_redundante': True, 'quem': u'José Silva Fernandes'}

# >>> redun_palavra_palavra(u'José Fernandes Silva', u'José Silva Fernandes Melo')
'eh_redundante': True, 'quem': u'José Silva Fernandes Melo'}


>>> redun_frase_frase(u"João conhece Heitor", u"João conhece Gomes")
False

>>> redun_frase_frase(u"João conhece", u"João conhece Gomes")
True

>>> redun_frase_frase(u"João conhece", u"João conhece Heitor")
True

>>> redun_frase_frase(u"João conhece Gomes", u"João conhece")
True

>>> redun_palavra_frase(u"João conhece", u"João conhece Gomes")
True

>>> redun_palavra_frase(u"João conhece Maria", u"João conhece Gomes")
False

>>> redun_palavra_frase(u"João Maria", u"João conhece Maria")
True

>>> redun_palavra_frase(u"João conhece Maria", u"João Maria")
False


# >>> redun_palavra_lista(u'João', [u'João Augusto'])
# True

# >>> redun_palavra_lista(u'João Augusto', [u'João Pereira'])
{}

# >>> redun_palavra_lista(u'João Augusto', [u'João Pereira', u'Augusto João'])
# True


>>> redun_frase_lista(u'João conhece', [u'João conhece Maria'])
True

>>> redun_frase_lista(u'João conhece', [u'Maria conhece João'])
False

>>> redun_frase_lista(u'João conhece', [u'Maria conhece João', u'Maria João conhece'])
True


>>> redun_palavra_frase_lista(u'João', [u'João Gomes'])
True

>>> redun_palavra_frase_lista(u'João Gomes', [u'João conhece Gomes'])
True

>>> redun_palavra_frase_lista(u'João Gomes Silva', [u'João conhece Gomes'])
False

>>> redun_palavra_frase_lista(u'João Gomes', [u'João Silva', u'Gomes João'])
True
'''


def redun_palavra_palavra(set1, set2):
    '''
    Redundancia entre palavra e palavra.

    Args:
        set1 (str): primeira palavra.
        set2 (str): segunda palavra.

    Returns:
        dict: Dicionário.
    '''
    cj1 = set(set1.split())
    cj2 = set(set2.split())
    if cj1.issubset(cj2) or cj2.issubset(set(cj1)):
        # Verifica quem é o redundante.
        # O maior é o redundante.
        maior = set1 if len(cj1) > len(cj2) else set2
        resposta = {'eh_redundante': True, 'quem': maior}
    else:
        resposta = {}
    return resposta


def redun_frase_frase(str1, str2):
    '''
    Redundancia entre frase e frase.

    Args:
        str1 (str): primeira frase.
        str2 (str): segunda frase.

    Returns:
        dict: Dicionário.
    '''
    cj1 = set(str1.split())
    cj2 = set(str2.split())
    if str1 in str2 or str2 in str1:
        # Verifica quem é o redundante.
        # O maior é o redundante.
        maior = str1 if len(cj1) > len(cj2) else str2
        resposta = {'eh_redundante': True, 'quem': maior}
    else:
        resposta = {}
    return resposta


def redun_palavra_frase(palavra, frase):
    '''
    Redundancia entre palavra e frase.

    Args:
        palavra (str): palavra.
        frase (str): frase.

    Returns:
        dict: Dicionário.
    '''
    _palavra = set(palavra.split())
    _frase = set(frase.split())
    if _palavra.issubset(_frase):
        # Verifica quem é o redundante.
        # O maior é o redundante.
        maior = frase if len(_frase) > len(_palavra) else palavra
        resposta = {'eh_redundante': True, 'quem': maior}
    else:
        resposta = {}
    return resposta


def redun_palavra_lista(palavra, palavras):
    '''
    Redundancia entre uma palavra e uma lista de palavras.

    Args:
        palavra (str): palavra.
        palavras (list): lista de palavras.

    Returns:
        bool: Se eh redundante ou nao.
    '''
    for _palavra in palavras:
        r = redun_palavra_palavra(palavra, _palavra)
    return r


def redun_frase_lista(frase, frases):
    '''
    Redundancia entre uma frase e uma lista de frases.

    Args:
        frase (str): frase.
        frases (list): lista de frases.

    Returns:
        bool: Se eh redundante ou nao.
    '''
    for _frase in frases:
        r = redun_frase_frase(frase, _frase)
    return r


def redun_palavra_frase_lista(palavra, frases):
    '''
    Redundancia entre uma palavra e uma lista de frases.

    Args:
        palavra (str): palavra.
        frases (list): lista de frases.

    Returns:
        bool: Se eh redundante ou nao.
    '''
    for _palavra in frases:
        r = redun_palavra_frase(palavra, _palavra)
    return r
