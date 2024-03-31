a =[1, 2, 3, 1, 2, 4, 4, 6, 8, 8,8]
a_avarage = sum(a)/len(a)

result = []

for number in a:
    if number >a_avarage:
        result.append(number)

print(result)

