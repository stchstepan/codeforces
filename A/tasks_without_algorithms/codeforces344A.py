n = int(input())
b = [input() for i in range(n)]
ans = []
running_count = 1
for i in range(n-1):
    if b[i]==b[i+1]:
        running_count+=1
    else:
        ans.append(running_count)
ans.append(running_count)
print(len(ans))