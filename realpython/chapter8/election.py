from random import random

elections, total = 10000, 0

# for i in range(elections):
#     total += random()

# average = total / elections
# print(average)


def election(chance_of_win):
    if random() <= chance_of_win:
        return 1
    return 0

for i in range(elections):
    total_wins_candidate_a = 0
    total_wins_candidate_a += election(0.87)  # region 1
    total_wins_candidate_a += election(0.65)  # region 2
    total_wins_candidate_a += election(0.17)  # region 3

    if total_wins_candidate_a > 1:
        # candidato A ganhou
        print('candidato A ganhou')
    else:
        # candidato B ganhou
        print('candidato B ganhou')
