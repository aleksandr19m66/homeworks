stroka =input("введите слово: ")

stroka_l =list(stroka)

stroka_l.reverse()
stroka_rev = ''.join(stroka_l)

if stroka_rev == stroka:
  print("Палиндром")
else:
  print("Не палиндром")