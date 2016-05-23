import random

''' zip example '''
x = [1, 2, 3]
y = ['Um', 'Dois', 'Tres']
r = list(zip(x, y))
print(r)

''' other example '''
led_index = random.random() * 10
li = list(range(10))
bl = list(range(0, 100, 10))
r = list(zip(li, bl))
print(r)
