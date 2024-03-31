 nums = int(input("Число двухзначное: "))
nums_set =set(str(nums))
if 9< nums < 100:
 if len(nums_set) == 1:
    print('Да это число ', nums)
 else:
    print('Нет')
else:
    print('Число не двухзначное!')