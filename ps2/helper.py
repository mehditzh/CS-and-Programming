import string
my_word = 's_ l_ m'
other_word = 'salam'

my_word = my_word.replace(' ', '')

words_match = True
my_word_letters = []
if len(my_word) == len(other_word):
    for i in range(len(my_word)):
        if my_word[i].isalpha():
            my_word_letters.append(my_word[i])
            if my_word[i] == other_word[i]:
                words_match = True
            else:
                words_match = False
                break
    for i in range(len(my_word)):
        if not my_word[i].isalpha():
            if other_word[i] in my_word_letters:
                words_match = False
                break
else: words_match = False

print(words_match)
guessed_word = ''
guessed_word += 'a'
guessed_word += '_ '
guessed_word += 'h'
guessed_word += 'h'
print(guessed_word.type())