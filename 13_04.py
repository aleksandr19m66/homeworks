seconds = int(input('Введите время в секундах: '))

ch = seconds // 3600
ss = seconds % 60
mm = (seconds - ch * 3600) // 60
print(ch,':',mm,':',ss,sep='')
print(f{ch}:{mm}:{ss})




