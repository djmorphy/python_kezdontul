# dictionary comperhensions - szotar megertesek
0

nevek = ["Andi", "Erika", "Zsofi"]
korok = [23, 45, 34]

#zip összepárosítja a nevek 0 index-et a korok 0 index-el
print(list((nevek, korok)))

#szotar letrehozas
adatok1 = {nev:kor for nev, kor in zip(nevek, korok)}
print(adatok1)

#csak az utilsó adatot szedte ki
adatok2 = {"nev":nev for nev in nevek}
print(adatok2)

#a nev stringet enumeralom (megszámozom). Enumerate-t meghívom egy listan az vissza adja az indexet
#Az indexet el is kell kapnom az az str(index)
adatok3 = {"nev" + str(index+1):nev for index, nev in enumerate(nevek)}
print(adatok3)


# a kulcs a szemely + index szám az enumarte fgv miatt.  Szótar value-ja egy tuple lett ami tartalmazza
#a nevet és a kor-t
#enumerate megszámozza amit a zip visszaadott és végül átloopolunk rajta
adatok4 = {"szemely" + str(index+1):(nev, kor) for index, (nev, kor) in enumerate(zip(nevek, korok))}
print("adat4")
print(adatok4)


adatok5 = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6}

#1 kondició belerakása
adatok5_v2 = {k:v for (k, v) in adatok5.items()}
print(adatok5_v2)

#c-től fog kezdődni
adatok5_v2 = {k:v for (k, v) in adatok5.items() if v >2}
print(adatok5_v2)

#ha nagyobb mint kettő és páros
adatok5_v2 = {k:v for (k, v) in adatok5.items() if v >2 if v %2 ==0}
print(adatok5_v2)

#ha 2-vel és 3-al osztható azaz a 6
adatok5_v2 = {k:v for (k, v) in adatok5.items() if v >2 if v %2 ==0 if v % 3 ==0}
print(adatok5_v2)