a, d = int(input()), 0
for i in range(0,a):
    b, c = map(int, input().split())
    if c-b>=2:
        d+=1
print(d)