a, b = map(int, input().split())
i = list(map(int, input().split()))
c = 0
for x in i:
    if x > b:
        c+=2
    else:
        c+=1
print(c)