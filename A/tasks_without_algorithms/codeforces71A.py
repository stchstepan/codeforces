print("Я - (не) работает")

n = int(input("Введите число: "))

words = []

while n > 0 and n < 101:
    n -= 1
    word = input("Введите слово: ")
    words.append(word)

for word in words:
    if len(word) > 10:
        word = list(word)
        chancge = len(word[0:-2])
        word = f"{word[0]}{chancge}{word[-1]}"
        print(word)
    else:
        print(word)

print("Андрей - работает")

for n in range(int(input())): #вводим n (n - целое число) и для всех (range) n выполняем:
  word = input()
  if len(word) > 10:
      print(f"{word[0]}{len(word[1:-1])}{word[-1]}")
      continue
  print(word)