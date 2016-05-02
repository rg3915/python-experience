phrase = input('Enter some text: ')
letters = {
    'a': '4',
    'b': '8',
    'e': '3',
    'l': '1',
    'o': '0',
    's': '5',
    't': '7'
}
for v in letters:
    phrase = phrase.replace(v, letters[v])
print(phrase)
