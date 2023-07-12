x = 0

for i in range(int(input())):
    for m in set(input()):
        if '+' in m:
            x += 1
        elif '-' in m:
            x -= 1

print(x)