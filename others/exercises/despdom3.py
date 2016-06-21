# despdom1.py - Calculadora de despesas domesticas
print 'Balanco de despesas domesticas'
Regis = float(raw_input('Quanto gastou Regis? '))
Roseli = float(raw_input('Quanto gastou Roseli? '))
print
total = Regis + Roseli
print 'Total de gastos = R$ %s.' % total
media = total / 2
print 'Gastos por pessoa = R$ %s.' % media
if Regis < media:
    diferenca = media - Regis
    print 'Regis deve pagar: R$ %s' % diferenca
elif Roseli < media:
    diferenca = media - Roseli
    print 'Roseli deve pagar: R$ %s' % diferenca
else:
    print 'Regis e Roseli gastaram a mesma quantia.'
