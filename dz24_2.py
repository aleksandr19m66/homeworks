stroka = input('Текст :')
s_strok = stroka.split(' ')

s_strok5 = []

for li in s_strok:
    if len(str(li))>5:
        s_strok5.append(li)
print(s_strok5)