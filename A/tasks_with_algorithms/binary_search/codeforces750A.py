n, k=map(int, input().split())
while ((10+5*n-5)/2)*n>240-k:
    n-=1
print(n)