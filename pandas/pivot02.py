import pandas as pd


answers = [
    ('user1', {'10': '39', '1': '1', '3': '9', '2': '5', '5': '18', '4': '16', '7': '25', '6': '21', '9': '35', '8': '31'}),
    ('user2', {'10': '40', '1': '2', '3': '10', '2': '6', '5': '19', '4': '17', '7': '26', '6': '22', '9': '36', '8': '32'}),
    ('user3', {'10': '41', '1': '3', '3': '11', '2': '7', '5': '20', '4': '18', '7': '27', '6': '23', '9': '37', '8': '33'}),
]
answers_data = []
for user, qa in answers:
    for q, a in sorted(qa.items()):
        answers_data.append(dict(user=user, question=q, answer=a))

df = pd.DataFrame(answers_data)
pv = df.pivot(index='user', columns='question', values='answer')
print(pv)
