#anonymus functions, lamda expressions - anonym fgv, lamda kepletek
#lamdba fgv a funkcinolási programozási dizájnba használjuk. Map, filter, reduce
def osszead1(a, b):
    return a+b

print(osszead1(10,15))

#lamdba fgv befogad két paramétert. És nem kell return kucslszó
osszead2 = lambda a,b: a+b

print(osszead2(25,20))

lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print()
paros = list(filter(lambda x: x % 2 ==0, lista))
print("Filter object: ")
print(paros)

print("for loop: ")
paros = (filter(lambda x: x % 2 ==0, lista))
for p in paros:
    print(p)

print("müveletek dictionary")
muveletek = {
    "add":lambda a,b: a+b,
    "sub":lambda a,b: a-b,
    "mult":lambda a,b: a*b,
    "div":lambda a,b: a/b
}

print(muveletek["add"](10,8))
add = muveletek["add"](10,8)
print(add)

add = muveletek["add"]
print(add(12, 8))

muvelet = muveletek["div"]
print(muvelet(12,8))