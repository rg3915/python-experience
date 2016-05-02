def invest(amount, rate, time):
    print('principal amount: $' + str(amount))
    print('annual rate of return: ' + str(rate))
    for i in range(1, time + 1):
        r = round(amount * (1 + rate) ** i, 9)
        print('year {}: ${}'.format(i, r))

invest(100, .05, 8)
invest(2000, .025, 5)
