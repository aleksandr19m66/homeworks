name =input("Введите имя: ")
name_list = name.split (',')

if len(name_list) == 0:
    print("no one likes this")
elif len(name_list) == 1:
    print(name_list[0], "likes this")
elif len(name_list) == 2:
    print(name_list[0], "and", name_list[1], "likes this")
elif len(name_list) == 3:
    print(name_list[0], ",", name_list[1], "and", name_list[2], "likes this")
elif len(name_list) > 2:
    print(name_list[0], ",", name_list[1], "and", len(name_list)-2, "others like this")

