kmh = {'speed1':100, 'speed2':92,'speed3':1030, 'speed4':46}
kmm = {a:round (b*1.609,2) for (a,b) in kmh.items()}
print(kmm)