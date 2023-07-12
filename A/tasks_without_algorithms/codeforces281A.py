# мое длинное и плохое решение

word = list(input())
word[0] = word[0].upper()
new_word = []
while word:
    letter = word.pop()
    new_word.append(letter)
new_word.reverse()
print(''.join(new_word))

# чужое - быстрое

s = input()
print(s[0].upper()+s[1:]) # оказывается, слово можно интерпритировать как словарь 