
def letter_histogram(word):
    dict = {}
    for letter in word:
        keys = dict.keys()
        if letter in keys:
            dict[letter] += 1
        else:
            dict[letter] = 1
    return dict 

print(letter_histogram('gkllkjljljljlglejmnsfksjfz'))


#another solution, but ask for the user inputs

user_input = input('Please enter a word: ')

lists = {}

for i in user_input:
    if i in lists:
        lists[i] += 1
    elif i not in lists:
        lists[i] = 1

print(lists)

