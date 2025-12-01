def palindrom(s):
    d=len(s)-1
    i=0
    pom=True
    while i<d and pom==True:
        if s[i]!=s[d]:
            pom=False
        else:
            i+=1
            d-=1
    if pom==True:
        print("TAK")
    else:
        print("NIE")
print("Sprawdzanie czy wyraz jest palindromem.")
s=input("Podaj wyraz: ")
palindrom(s)