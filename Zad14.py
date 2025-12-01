print("Konwersja liczb między systemami 2,4,8,10,16")

s1 = int(input("Podaj system liczby: "))
s2 = int(input("Podaj system docelowy: "))
x = input("Podaj liczbę: ")

dec = int(x, b1)

cyfry = "0123456789ABCDEF"
wynik = ""
n = dec
if n == 0:
    wynik = "0"
else:
    while n > 0:
        wynik=digits[n%s2]+wynik
        n=n//s2

print("wynik:", wynik)
