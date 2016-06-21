# despdom1.py - Calculadora de despesas domesticas
print 'Balanco de despesas domesticas'
Regis = raw_input('Quanto gastou Regis? ')
Roseli = raw_input('Quanto gastou Roseli? ')
total = float(Regis) + float(Roseli)
print 'Total de gastos = R$ %s.' % total
media = total / 2
print 'Gastos por pessoa = R$ %s.' % media
