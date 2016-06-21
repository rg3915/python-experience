# somadora3.py - somadora infinita - versao 3

print 'Digite os valores a somar seguidos de .'
print 'para encerrar apenas .'
total = 0
while 1:
    try:
        n = float(raw_input(':'))
        total += n
    except:
        break
print 'TOTAL: %s' % total
