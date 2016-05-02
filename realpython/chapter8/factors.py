number = int(input('Enter a positive integer: '))


def factor(number, divisor):
    if number % divisor:
        return False
    return True


for i in range(1, number + 1):
    if factor(number, i):
        print('{} is a divisor of {}'.format(i, number))
