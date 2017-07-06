import pandas as pd


users = ['user1', 'user2', 'user3']
questions = [1, 3, 9, 6, 7, 5, 4, 2, 8, 10, ]
answers = [
    {"q10": "39", "q1": "1", "q3": "9", "q2": "5", "q5": "18", "q4": "16", "q7": "25", "q6": "21", "q9": "35", "q8": "31"},
    {"q10": "40", "q1": "2", "q3": "10", "q2": "6", "q5": "19", "q4": "17", "q7": "26", "q6": "22", "q9": "36", "q8": "32"},
    {"q10": "41", "q1": "3", "q3": "11", "q2": "7", "q5": "20", "q4": "18", "q7": "27", "q6": "23", "q9": "37", "q8": "33"},
]
answers_data = []
t = tuple(zip(users, answers))
for u, ca in t:
    for q, a in sorted(ca.items()):
        answers_data.append(dict(user=u, question=q, answer=a))

df = pd.DataFrame(answers_data)
pv = df.pivot(index='user', columns='question', values='answer')
print(pv)
