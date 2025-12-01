def Ekl(x, y):  #nwd
    while y != 0:
        x, y = y, x % y
    return x

def uprosc(licz, mian): #uproszczenie ulamka
    nwd = Ekl(abs(licz), abs(mian))
    return licz // nwd, mian // nwd

print("podaj dane ułamków:")

licz_1 = int(input("licznik 1: "))
mian_1 = int(input("mianownik 1: "))
licz_2 = int(input("licznik 2: "))
mian_2 = int(input("mianownik 2: "))

#suma
s_l = licz_1 * mian_2 + licz_2 * mian_1
s_m = mian_1 * mian_2
s_l, s_m = uprosc(s_l, s_m)

#roznica
r_l = licz_1 * mian_2 - licz_2 * mian_1
r_m = mian_1 * mian_2
r_l, r_m = uprosc(r_l, r_m)

#iloczyn
i_l = licz_1 * licz_2
i_m = mian_1 * mian_2
i_l, i_m = uprosc(i_l, i_m)

#iloraz
d_l = licz_1 * mian_2
d_m = mian_1 * licz_2
d_l, d_m = uprosc(d_l, d_m)

print("wyniki:")
print("suma: ",s_l/s_m)
print("różnica: ",r_l/r_m)
print("iloczyn: ",i_l/i_m)
print("iloraz: ",d_l/d_m)