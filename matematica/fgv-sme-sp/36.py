# 36
import time

jogada = {
    'Falta A': 590,
    'Pênalti': 785,
    'Gol I': 1350,
    'Gol II': 2690,
    'Falta B': 4332,
    'Bicicleta': 5960,
}


def convert_seconds_to_hms(seconds):
    # http://stackoverflow.com/a/24507708/802542
    return time.strftime("%H:%M:%S", time.gmtime(seconds))

print('Falta A: ' + convert_seconds_to_hms(jogada['Falta A']))
print('Pênalti: ' + convert_seconds_to_hms(jogada['Pênalti']))
print('Gol I: ' + convert_seconds_to_hms(jogada['Gol I']))
print('Gol II: ' + convert_seconds_to_hms(jogada['Gol II']))
print('Falta B: ' + convert_seconds_to_hms(jogada['Falta B']))
print('Bicicleta: ' + convert_seconds_to_hms(jogada['Bicicleta']))
