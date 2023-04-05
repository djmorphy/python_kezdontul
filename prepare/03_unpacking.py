#iterable unpacking - iterálható obj kicsomagolása - lista, tuple, string - __iter__()


lista1 = range(10)
print(lista1)
print(list(lista1))
print(*lista1) #unpacking operator


#lista1 = [1,2,3,4]

#lista2 = lista1  #referencia alapján hivatkozik. Ua memóriaterületre mutatt mind a kettő lista.
#lista2[0] = 87
#print(lista1)
#print(lista2)

lista1 = [1,2,3,4]
lista2 = [*lista1]

lista2[0] = 87

print(lista1)
print(lista2)


def func(*args, **kwargs):
# kwarg= key word arguments
    print(args)
    print(kwargs)

func(10,20,30,40)
func(10,20,30,40, {"nev1":"Adni", "nev2":"Aniko"})
func(10,20,30,40, **{"nev1":"Adni", "nev2":"Aniko"}) #párban nyomja ki a két csillag miatt

nevek = ["Andi", "Eniko", "Zsofi", "Erika", "Aniko"]
korok = [25, 28, 41, 49, 18]

#ezzel igy tulképp egy tuple-be összefűzöm
nev_kor = [*nevek], [*korok]
print(nev_kor)

#A sztringet elemeire bontottam
szoveg = "Hello Hogy vagy?"
szoveg_lista = [*szoveg]
print(szoveg_lista)

#A szétbontott sztring "visszacsomagolása"
udv = "".join(szoveg_lista)
print(szoveg_lista) #szétbontott
print(udv) #visszaállított