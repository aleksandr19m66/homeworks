#1
a = int(input("Vvedite a = "))
b = int(input("Vvedite b = "))

c = a
a = b
b = c

print("a = ", a)
print("b = ", b)

#2
storona = float(input("Vvedite storonu kvadrata - "))
print("diagohal: ", "%.1f"%(storona*(2)**0.5))
print("ploschad: ", "%.1f"%(storona**2))
print("perimetr: ", "%.1f"%(4*storona))

#3
n = int(input("Vvedite n = "))
print(n,"+",n*10+n,"+",n*100+n*10+n," = ",3*n+2*n*10+n*100)