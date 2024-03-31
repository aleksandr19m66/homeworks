stroka = input('Текст :')
s_strok = stroka.split(' ')

s_strok_b = []
def chisla(sp):
     for _ in s_strok:
       if (str(_)).isdigit():
        s_strok_b.append(_)
     return s_strok_b
print(chisla(s_strok))