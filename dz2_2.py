number =input("Введите числo: ")
number_list = list (number)

number_list.sort(reverse = True)

number_max = int(''.join(map(str, number_list)))

print(number_max)
