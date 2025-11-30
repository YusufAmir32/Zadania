def na_dec(x, s):
    wynik=0
    dlugosc=len(str(x))
    for i in range(dlugosc):
        cyfra=int(x[i])
        potega=dlugosc-1-i
        wynik=wynik+cyfra*(s**potega)
    print("wynik: ",wynik)

x = str(input("Podaj liczbe: "))
s = int(input("Podaj system liczbowy: "))
na_dec(x, s)