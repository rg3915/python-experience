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
True

>>> redun_palavra_palavra(u'João Augusto', u'João Augusto Pereira')
True

>>> redun_palavra_palavra(u'João Augusto', u'João Pereira Augusto')
True

>>> redun_palavra_palavra(u'João Augusto', u'João Pereira')
False

>>> redun_palavra_palavra(u'João Maria', u'Maria João')
True

>>> redun_palavra_palavra(u'Maria João', u'João Maria')
True

>>> redun_palavra_palavra(u'Maria João Silva', u'João Maria')
True

>>> redun_palavra_palavra(u'José Augusto', u'José Silva')
False

>>> redun_palavra_palavra(u'José Augusto', u'João Augusto')
False

>>> redun_palavra_palavra(u'João Silva', u'José Silva')
False

>>> redun_palavra_palavra(u'João Silva', u'João Augusto')
False

>>> redun_palavra_palavra(u'José Silva', u'João Augusto')
False

>>> redun_palavra_palavra(u'José Fernandes', u'José Fernandes Silva')
True

>>> redun_palavra_palavra(u'José Fernandes', u'José Silva Fernandes')
True

>>> redun_palavra_palavra(u'José Fernandes Silva', u'José Silva Fernandes')
True

>>> redun_palavra_palavra(u'José Fernandes Silva', u'José Silva Fernandes Melo')
True


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


>>> redun_palavra_lista(u'João', [u'João Augusto'])
True

>>> redun_palavra_lista(u'João Augusto', [u'João Pereira'])
False

>>> redun_palavra_lista(u'João Augusto', [u'João Pereira', u'Augusto João'])
True


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
        bool: Se eh redundante ou nao.
    '''
    if set(set1).issubset(set(set2)) or set(set2).issubset(set(set1)):
        return True
    return False


def redun_frase_frase(str1, str2):
    '''
    Redundancia entre frase e frase.

    Args:
        str1 (str): primeira frase.
        str2 (str): segunda frase.

    Returns:
        bool: Se eh redundante ou nao.
    '''
    if str1 in str2 or str2 in str1:
        return True
    return False


def redun_palavra_frase(palavra, frase):
    '''
    Redundancia entre palavra e frase.

    Args:
        palavra (str): palavra.
        frase (str): frase.

    Returns:
        bool: Se eh redundante ou nao.
    '''
    if set(palavra).issubset(set(frase)):
        return True
    return False


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
