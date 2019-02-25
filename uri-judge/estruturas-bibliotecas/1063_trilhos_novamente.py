# https://www.urionlinejudge.com.br/judge/pt/problems/view/1063
def rails_again(rail_a, rail_b):
    rail_a.reverse()
    rail_b.reverse()
    station = []
    sequence = []
    highest_active_position = len(rail_b) - 1
    while len(rail_a):
        station.append(rail_a.pop())
        sequence.append('I')
        while station and station[-1] == rail_b[highest_active_position]:
            station.pop()
            highest_active_position -= 1
            sequence.append('R')
    if station:
        sequence.append(' Impossible')
    return ''.join(sequence)


def test():
    input_sequence = ['e', 't', 'd', 'a']
    desired_sequence = ['d', 'a', 't', 'e']
    assert rails_again(input_sequence, desired_sequence) == 'IIIRIRRR'

    input_sequence = ['o', 's', 't', 'a', 'p']
    desired_sequence = ['p', 'a', 't', 'o', 's']
    assert rails_again(input_sequence, desired_sequence) == 'IIIIIRRR Impossible'


def uri_format():
    while True:
        number_wagons = int(input())
        if not number_wagons:
            break
        input_sequence = [x for x in input().split()]
        desired_sequence = [x for x in input().split()]
        print(rails_again(input_sequence, desired_sequence))


if __name__ == '__main__':
    test()
    uri_format()
