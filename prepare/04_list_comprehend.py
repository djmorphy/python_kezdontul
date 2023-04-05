#list comprehension - lista megertesek

szamok = []
for i in range(20):
    szamok.append(i)

print(szamok)

szamok = [x for x in range(15)]
print(szamok)

paros = [x for x in range(20) if x % 2==0]
print(paros)

paratlan = [x for x in range(20) if x % 2 !=0]
print(paratlan)

nevek = ["andi", "eniko", "zsofi", "erika", "aniko"]
print(nevek)

#lehetne loopal de egyszerűbb list compherension-el

nevek = [nev.capitalize() for nev in nevek]
print(nevek)

nevek_A = [nev for nev in nevek if nev.startswith("A")]
print(nevek_A)