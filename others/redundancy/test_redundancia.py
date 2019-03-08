# -*- coding: utf-8 -*-

import unittest
from itertools import chain
from redundancia import (
    redun_palavra_palavra,
    redun_frase_frase,
    redun_palavra_frase,
    redun_palavra_lista,
    redun_frase_lista,
    redun_palavra_frase_lista,
)

'''
Procura por redundância entre:

* Palavra e Palavra
* Frase e Frase
* Palavra e Frase

# Palavra e Palavra

Se um set é subset da outra. Usar set().

Exemplo:

João
João Augusto
True

João Augusto
João Augusto Pereira
True

João Augusto
João Pereira Augusto
True

João Augusto
João Pereira
False

José Augusto
João Silva
José Silva
João Augusto
False

José Fernandes
José Fernandes Silva
José Silva Fernandes
True


# Frase e Frase

Se uma string é substring da outra. Comparar strings.

Exemplo:

"João conhece Heitor"
"João conhece Gomes"
False

"João conhece"
"João conhece Gomes"
True.

"João conhece"
"João conhece Heitor"
True.

"João conhece Gomes"
"João conhece"
True.


# Palavra e Frase

Se o set de palavras é subset da frase. Somente set(P) <= set(F).

palavra = "João conhece"
frase = "João conhece Gomes"
True

palavra = "João conhece Maria"
frase = "João conhece Gomes"
False

palavra = "João Maria"
frase = "João conhece Maria"
True


Parte 2:

1. Dada uma palavra e um conjunto de palavras,
informar se essa palavra é redundante.

palavra = João
palavras = [
    'João Augusto',
]
True

palavra = João Augusto
palavras = [
    'João Pereira',
]
False

palavra = João Silva
palavras = [
    'João Augusto',
    'João Augusto Silva',
]
True


2. Dada uma frase e uma lista de frases,
informar se essa frase é redundante.

frase = 'João conhece'
frases = [
    'João conhece Maria'
]
True

frase = 'João conhece'
frases = [
    'Maria conhece João',
]
False

frase = 'João conhece'
frases = [
    'Maria conhece João',
    'Maria João conhece',
]
True


3. Dada uma palavra e uma lista de frases,
informar se essa palavra é redundante.

palavra = 'João'
frases = ['João Gomes']
True

palavra = 'João Gomes'
frases = ['João conhece Gomes']
True

palavra = 'João Gomes Silva'
frases = ['João conhece Gomes']
False

palavra = 'João Gomes'
frases = ['João Silva', 'Gomes João']
True


Parte 3:

Mostrar quais itens devem ser eliminados da redundância.
'''


class RedundanciaPPTest(unittest.TestCase):
    '''
    Redundância entre palavra e palavra.
    '''

    def test_pp_aaa(self):
        set1 = 'aaa'
        set2 = 'Amanda'
        esperado = {}
        self.assertEqual(redun_palavra_palavra(set1, set2), esperado)

    def test_pp_joao(self):
        set1 = 'João'
        set2 = 'João Augusto'
        esperado = {'eh_redundante': True, 'quem': set2}
        self.assertEqual(redun_palavra_palavra(set1, set2), esperado)

    def test_pp_joao_augusto(self):
        set1 = 'João Augusto'
        set2 = 'João Augusto Pereira'
        esperado = {'eh_redundante': True, 'quem': set2}
        self.assertEqual(redun_palavra_palavra(set1, set2), esperado)

    def test_pp_joao_augusto2(self):
        set1 = 'João Augusto'
        set2 = 'João Pereira Augusto'
        esperado = {'eh_redundante': True, 'quem': set2}
        self.assertEqual(redun_palavra_palavra(set1, set2), esperado)

    def test_pp_joao_augusto3(self):
        set1 = 'João Augusto'
        set2 = 'João Pereira'
        esperado = {}
        self.assertEqual(redun_palavra_palavra(set1, set2), esperado)

    def test_pp_joao_maria1(self):
        set1 = 'João Maria'
        set2 = 'Maria João'
        esperado = {'eh_redundante': True, 'quem': set2}
        self.assertEqual(redun_palavra_palavra(set1, set2), esperado)

    def test_pp_joao_maria2(self):
        set1 = 'Maria João'
        set2 = 'João Maria'
        esperado = {'eh_redundante': True, 'quem': set2}
        self.assertEqual(redun_palavra_palavra(set1, set2), esperado)

    def test_pp_joao_maria3(self):
        set1 = 'Maria João Silva'
        set2 = 'João Maria'
        esperado = {'eh_redundante': True, 'quem': set1}
        self.assertEqual(redun_palavra_palavra(set1, set2), esperado)

    def test_pp_joao_augusto_jose_silva2(self):
        set1 = 'José Augusto'
        set3 = 'José Silva'
        esperado = {}
        self.assertEqual(redun_palavra_palavra(set1, set3), esperado)

    def test_pp_joao_augusto_jose_silva3(self):
        set1 = 'José Augusto'
        set4 = 'João Augusto'
        esperado = {}
        self.assertEqual(redun_palavra_palavra(set1, set4), esperado)

    def test_pp_joao_augusto_jose_silva4(self):
        set2 = 'João Silva'
        set3 = 'José Silva'
        esperado = {}
        self.assertEqual(redun_palavra_palavra(set2, set3), esperado)

    def test_pp_joao_augusto_jose_silva5(self):
        set2 = 'João Silva'
        set4 = 'João Augusto'
        esperado = {}
        self.assertEqual(redun_palavra_palavra(set2, set4), esperado)

    def test_pp_joao_augusto_jose_silva6(self):
        set3 = 'José Silva'
        set4 = 'João Augusto'
        esperado = {}
        self.assertEqual(redun_palavra_palavra(set3, set4), esperado)

    def test_pp_jose_fernandes1(self):
        set1 = 'José Fernandes'
        set2 = 'José Fernandes Silva'
        esperado = {'eh_redundante': True, 'quem': set2}
        self.assertEqual(redun_palavra_palavra(set1, set2), esperado)

    def test_pp_jose_fernandes2(self):
        set1 = 'José Fernandes'
        set2 = 'José Silva Fernandes'
        esperado = {'eh_redundante': True, 'quem': set2}
        self.assertEqual(redun_palavra_palavra(set1, set2), esperado)

    def test_pp_jose_fernandes3(self):
        set1 = 'José Fernandes Silva'
        set2 = 'José Silva Fernandes'
        esperado = {'eh_redundante': True, 'quem': set2}
        self.assertEqual(redun_palavra_palavra(set1, set2), esperado)

    def test_pp_jose_fernandes4(self):
        set1 = 'José Fernandes Silva'
        set2 = 'José Silva Fernandes Melo'
        esperado = {'eh_redundante': True, 'quem': set2}
        self.assertEqual(redun_palavra_palavra(set1, set2), esperado)

    def test_pp_submarino(self):
        set1 = 'submarino'
        set2 = 'submarino amarelo'
        esperado = {'eh_redundante': True, 'quem': set2}
        self.assertEqual(redun_palavra_palavra(set1, set2), esperado)


class RedundanciaFFTest(unittest.TestCase):
    '''
    Redundância entre frase e frase.
    '''

    def test_ff1(self):
        str1 = "João conhece Heitor"
        str2 = "João conhece Gomes"
        esperado = {}
        self.assertEqual(redun_frase_frase(str1, str2), esperado)

    def test_ff2(self):
        str1 = "João conhece"
        str2 = "João conhece Gomes"
        esperado = {'eh_redundante': True, 'quem': str2}
        self.assertEqual(redun_frase_frase(str1, str2), esperado)

    def test_ff3(self):
        str1 = "João conhece"
        str2 = "João conhece Heitor"
        esperado = {'eh_redundante': True, 'quem': str2}
        self.assertEqual(redun_frase_frase(str1, str2), esperado)

    def test_ff4(self):
        str1 = "João conhece Gomes"
        str2 = "João conhece"
        esperado = {'eh_redundante': True, 'quem': str1}
        self.assertEqual(redun_frase_frase(str1, str2), esperado)

    def test_ff5(self):
        str1 = "Teste de frases"
        str2 = "teste de"
        esperado = {'eh_redundante': True, 'quem': str1}
        self.assertEqual(redun_frase_frase(str1, str2), esperado)

    def test_ff6(self):
        str1 = "baba cade"
        str2 = "baba"
        esperado = {'eh_redundante': True, 'quem': str1}
        self.assertEqual(redun_frase_frase(str1, str2), esperado)


class RedundanciaPFTest(unittest.TestCase):
    '''
    Redundância entre palavra e frase.
    '''

    def test_pf1(self):
        palavra = "João conhece"
        frase = "João conhece Gomes"
        esperado = {'eh_redundante': True, 'quem': frase}
        self.assertEqual(redun_palavra_frase(palavra, frase), esperado)

    def test_pf2(self):
        palavra = "João conhece Maria"
        frase = "João conhece Gomes"
        esperado = {}
        self.assertEqual(redun_palavra_frase(palavra, frase), esperado)

    def test_pf3(self):
        palavra = "João Maria"
        frase = "João conhece Maria"
        esperado = {'eh_redundante': True, 'quem': frase}
        self.assertEqual(redun_palavra_frase(palavra, frase), esperado)

    def test_pf4(self):
        palavra = "João conhece Maria"
        frase = "João Maria"
        esperado = {}
        self.assertEqual(redun_palavra_frase(palavra, frase), esperado)

    def test_pf5(self):
        palavra = "Americanas"
        frase = "Americanas teste"
        esperado = {'eh_redundante': True, 'quem': frase}
        self.assertEqual(redun_palavra_frase(palavra, frase), esperado)

    def test_pp_submarino1(self):
        palavra = 'submarino'
        frase = 'submarino amarelo'
        esperado = {'eh_redundante': True, 'quem': frase}
        self.assertEqual(redun_palavra_frase(palavra, frase), esperado)

    def test_pp_submarino2(self):
        palavra = 'submarino verde amarelo'
        frase = 'submarino verde'
        esperado = {}
        self.assertEqual(redun_palavra_frase(palavra, frase), esperado)

    def test_pp_submarino3(self):
        palavra = 'submarino verde'
        frase = 'submarino verde amarelo'
        esperado = {'eh_redundante': True, 'quem': frase}
        self.assertEqual(redun_palavra_frase(palavra, frase), esperado)


class RedundanciaPPListaTest(unittest.TestCase):
    '''
    Dada uma palavra e uma lista de palavras, informar se essa palavra é redundante.
    '''

    def test_ppl1(self):
        palavra = 'João'
        palavras = ['João Augusto']
        esperado = {'eh_redundante': True, 'quem': palavras[0]}
        self.assertEqual(redun_palavra_lista(palavra, palavras), esperado)

    def test_ppl2(self):
        palavra = 'João Augusto'
        palavras = ['João Pereira']
        esperado = {}
        self.assertEqual(redun_palavra_lista(palavra, palavras), esperado)

    def test_ppl3(self):
        palavra = 'João Augusto'
        palavras = ['João Pereira', 'Augusto João']
        esperado = {'eh_redundante': True, 'quem': palavras[-1]}
        self.assertEqual(redun_palavra_lista(palavra, palavras), esperado)


class RedundanciaFFListaTest(unittest.TestCase):
    '''
    Dada uma frase e uma lista de frases, informar se essa frase é redundante.
    '''

    def test_ffl1(self):
        frase = 'João conhece'
        frases = ['João conhece Maria']
        esperado = {'eh_redundante': True, 'quem': frases[-1]}
        self.assertEqual(redun_frase_lista(frase, frases), esperado)

    def test_ffl2(self):
        frase = 'João conhece'
        frases = ['Maria conhece João']
        esperado = {}
        self.assertEqual(redun_frase_lista(frase, frases), esperado)

    def test_ffl3(self):
        frase = 'João conhece'
        frases = [
            'Maria conhece João',
            'Maria João conhece'
        ]
        esperado = {'eh_redundante': True, 'quem': frases[-1]}
        self.assertEqual(redun_frase_lista(frase, frases), esperado)


class RedundanciaPFListaTest(unittest.TestCase):
    '''
    Dada uma palavra e uma lista de frases, informar se essa palavra é redundante.
    '''

    def test_pfl1(self):
        palavra = 'João'
        frases = ['João Gomes']
        esperado = {'eh_redundante': True, 'quem': frases[-1]}
        self.assertEqual(redun_palavra_frase_lista(palavra, frases), esperado)

    def test_pfl2(self):
        palavra = 'João Gomes'
        frases = ['João conhece Gomes']
        esperado = {'eh_redundante': True, 'quem': frases[-1]}
        self.assertEqual(redun_palavra_frase_lista(palavra, frases), esperado)

    def test_pfl3(self):
        palavra = 'João Gomes Silva'
        frases = ['João conhece Gomes']
        esperado = {}
        self.assertEqual(redun_palavra_frase_lista(palavra, frases), esperado)

    def test_pfl4(self):
        palavra = 'João Gomes'
        frases = ['João Silva', 'Gomes João']
        esperado = {'eh_redundante': True, 'quem': palavra}
        self.assertEqual(redun_palavra_frase_lista(palavra, frases), esperado)


if __name__ == '__main__':
    unittest.main()
