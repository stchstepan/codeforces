# Решение 1 (до того, как узнал про арифметическую прогрессию)

k,n,w=map(int,input().split())
x = w*k
while w > 0:
    w -= 1
    x += w*k
if n-x > 0:
    print(0)
else:
    print((abs(n-x)))

# Решение 2 (после того, как узнал про арифметическую прогрессию)

k,n,w=map(int,input().split())
print(max(0,w*(w+1)*k//2-n))