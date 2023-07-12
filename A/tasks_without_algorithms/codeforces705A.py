a = int(input())
b = 'I hate '
for i in range(2, a+1):
    if i % 2 == 0:
        b += 'that I love '
    if i % 2 != 0:
        b += 'that I hate '
print(f"{b}it")