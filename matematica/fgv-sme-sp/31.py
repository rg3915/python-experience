#-*- coding: utf-8 -*-
from __future__ import division 
import math
from random import choice

#a = 1 / 6
#print(round(a, 1))

class Dice:
	
	def __init__(self):
		self._numbers = [int(n) for n in range(1, 7)]

	def roll(self):
		return choice(self._numbers)

	def __len__(self):
		return len(self._numbers)

	def __iter__(self):
		return iter(self._numbers)


def to_percent(prob, total):
	percentage = round((prob / total) * 100, 2)
	return str(percentage) + '%'

def to_absolute(prob, total):
	return str(prob) + ' / ' + str(total)

def count_all_possibilities(rolls=1):
	return len(Dice()) ** rolls

def get_probabilities_for_sum(rolls=1, _sum=0, convert_to=to_absolute):

	if rolls == 1:
		return convert_to(1, 6)
	else:
		_get_possibilities_for_many_rolls(_sum, count_all_possibilities(rolls))


def _get_possibilities_for_many_rolls(_sum, rolls=2, convert_to=to_absolute):
	
	if _sum in range(2, 8):
		return str(_sum - 1) + ' / 36'
	elif _sum in range(8, 13):
		'''
		   A fórmula abaixo representa a seguinte ideia:
		   Após soma 7 (que é a maior probabilidade com dois dados), 
		   temos um declínio de chances, que segue o seguinte padrão:
		      - Soma 8: 5 possibilidades em 36 : (5 / 36)
		      - Soma 9: 4 possibilidades em 36 : (4 /36)
		      - Soma 10: 3 possibilidades em 36 : (3 /36)
		      - Soma 11: 2 possibilidades em 36: (2 / 36)
		      - Soma 12: 1 possibilidade em 36: (1 / 36)
		   
		   Então, criei um fórmula para obter o denominador (ou quantas possibilidades em 36 a soma representa).

		   O denominador ou probabilidade de cair o número é a soma (_sum) menos duas vezes a diferença entre a soma(_sum) e a soma com maior probabilidade de cair(no caso, o número 7) somadno à um


		   Para ficar, mais claro, segue um exemplo concreto:
           
		   Quando a soma for 8:
		   onde
		   _sum = 8
		   Soma com maior probabilidade = 7


		   8 - (2 * (8 - 7) + 1)
			# 8 - (2 * 1 + 1)
			# 8 - 3 = 5

			Então, as chances de cair são 5 para soma 8. (5 / 36)


		'''
		HIGHEST_PROBABILITY = 7
		PROBABILITY_FOR_NUM = _sum - (2 * (_sum - HIGHEST_PROBABILITY) + 1)
		return convert_to(PROBABILITY_FOR_NUM, 36)

	return '1 / 36'


if __name__ == '__main__':
	#To percent tests
	assert to_percent
	assert to_percent(1, 6) == '16.67%'
	assert to_percent(2, 6) == '33.33%'
    
	#To absolute tests
	assert to_absolute(1, 6) == '1 / 6'
	assert to_absolute(2, 3) == '2 / 3'


    #Dice tests 
	dice = Dice()
	expected_dice_range = [1, 2, 3, 4, 5, 6]

	assert dice._numbers
	assert dice._numbers == expected_dice_range
	assert len(dice) == 6

	assert dice.roll
	assert dice.roll() in expected_dice_range

	#Total possibilities tests
	assert count_all_possibilities
	assert count_all_possibilities() == 6
	assert count_all_possibilities(rolls=2) == 36
	assert count_all_possibilities(rolls=3) == 216
	
	assert _get_possibilities_for_many_rolls(_sum=2, rolls=2) == '1 / 36'	
	assert _get_possibilities_for_many_rolls(_sum=4, rolls=2) == '3 / 36'
	assert _get_possibilities_for_many_rolls(_sum=7, rolls=2) == '6 / 36'

	assert _get_possibilities_for_many_rolls(_sum=8, rolls=2) == '5 / 36'
	assert _get_possibilities_for_many_rolls(_sum=9, rolls=2) == '4 / 36'
	assert _get_possibilities_for_many_rolls(_sum=10, rolls=2) == '3 / 36'


	assert get_probabilities_for_sum(rolls=1, _sum=1) == '1 / 6'
	assert get_probabilities_for_sum(rolls=1, _sum=2) == '1 / 6'
	assert get_probabilities_for_sum(rolls=1, _sum=3) == '1 / 6'
	assert get_probabilities_for_sum(rolls=1, _sum=3) == '1 / 6'

	assert get_probabilities_for_sum(rolls=1, _sum=5, convert_to=to_percent) == '16.67%'



	#assert get_probabilites_for_sum(rolls=2, _sum=2) == '1 / 36'


   #Tests for calculate sum probabilities






