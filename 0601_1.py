array = "1 2 -3 45 5 6 7 81 9 "
array_list=list(map(int, array.split()))
print(array_list)
result = (min(array_list),max(array_list))
print(result)