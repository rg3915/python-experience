# somadora1.py - somadora infinita - versao 1

print 'Digite os valores a somar seguidos de .'
print 'para encerrar digite zero: 0'
n = float(raw_input(':'))
total = n
while n:
    n = float(raw_input(':'))
    total += n
print 'TOTAL: %s' % total
