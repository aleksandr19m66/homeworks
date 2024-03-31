 def ss(sp):
    s = True
    for li in sp:
        if li < 0:
            s = False
            break
    return s
wek = [2,3,54,-2,35,9]
print(ss(wek))