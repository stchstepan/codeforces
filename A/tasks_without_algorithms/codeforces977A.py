a = list(map(int, input().split()))
for c in range(0, a[1]):
    if a[0]%10==0:
        a[0]/=10
    else:
        a[0]-=1
print(int(a[0]))