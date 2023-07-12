t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    answ = 0 
    if a and b >= 1 and a+b >= 4:
        d = min(a, b)
        if ((a+b)-2*d)/d >= 2:
            print(d)
        else:
            while ((a+b)-2*d)/d < 2:
                d-=1
                print(d)
            print(d)
    else:
        print(0)

# t = int(input())
# for i in range(t):
#     a, b = map(int, input().split())
#     answ = 0 
#     if a and b >= 1 and a+b >= 4:
#         d = min(a, b)
#         if ((a+b)-2*d)/d >= 2:
#             print(d)
#         else:
#             while ((a+b)-2*d)/d < 2:
#                 d-=1
#             print(d)
#     else:
#         print(0)