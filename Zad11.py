def z_dec(x, s):
    if x==0:
        print(0)
    cyfry="0123456789ABCDEF"
    wynik=""
    while x > 0:
        wynik=cyfry[x%s]+wynik
        x=x//s
    print(wynik)

x=int(input("podaj liczbę: "))
s=int(input("podaj system docelowy (2-16): "))
z_dec(x,s)