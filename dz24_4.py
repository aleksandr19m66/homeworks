s_chisel = [12,3,4,5,6,7]

summa_chet_chisel = 0

for li in s_chisel:
    if li % 2 ==0:
      summa_chet_chisel+=li**2
print(summa_chet_chisel)