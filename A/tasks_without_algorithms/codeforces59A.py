word = input()
counter_upper = 0
couner_lower = 0
for i in word:
    if i == i.upper():
        counter_upper += 1
    elif i != i.upper():
        couner_lower += 1
if counter_upper > couner_lower:
    print(word.upper())
elif counter_upper < couner_lower or counter_upper == couner_lower:
    print(word.lower())