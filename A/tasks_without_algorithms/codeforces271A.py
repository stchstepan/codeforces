a = int(input())
b = a+1
while len(str(b)) > len(set(str(b))):
    b+=1
print(b)