'''
Os pontos (x,y) que pertencem à figura H (quarto de círculo no primeiro
quadrante) são tais que x >= 0, y >= 0 e x² + y² <= 1.
Dados n pontos reais (x,y), verificar se cada ponto pertence ou não a H.
'''

import unittest

n = int(input('Digite um número:'))


def region(x, y):
    if x >= 0 and y >= 0 and x * x + y * y <= 1:
        return True
    return False

for i in range(n):
    x = float(input())
    y = float(input())
    if region(x, y):
        print('({},{}) pertence a H.'.format(x, y))
    else:
        print('({},{}) não pertence a H.'.format(x, y))


class TestRegion(unittest.TestCase):

    def test_axis_x(self):
        self.assertEqual(region(1, 0), True)

    def test_axis_y(self):
        self.assertEqual(region(0, 1), True)

    def test_point_2(self):
        self.assertEqual(region(1, 1), False)

    def test_point_middle(self):
        self.assertEqual(region(0.5, 0.5), True)
