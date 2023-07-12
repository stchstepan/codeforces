n, k = map(int, input().split())
points = [int(i) for i in input().split()]
answ = [point for point in points if point >= points[k-1] and point > 0] #просто считаем кол-во элементов > или 
#>= баллам последнего места, при этом эти баллы должны быть > 0
print(len(answ))