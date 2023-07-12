a = int(input())
b, c = [], []
for i in range(0, a):
    out, inp = map(int, input().split())
    b.append(inp-out)
del b[-1]
c.append(b[0])
for i in b[1:]:
    x = b[0] + i
    b.remove(i)
    b[0] = x  
    c.append(x)
print(max(c))