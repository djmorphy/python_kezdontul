#functions as first class citizen Egy fgv bemeneti paramétere lehet egy másik fgv
import  math

#szam = 10

"""
class Szemely:
    def __init__(self, nev):
        self.nev = nev

sz1 = Szemely("Andi")

def func1(sz):
    print(sz.nev)

func1(sz1)

"""

def negyzet(x):
    return x*x

def gyok(x):
    #két csillag a hatvanyozás
    return x**0.5

def muvelet(func, szam):
    return func(szam)

m1 = muvelet(negyzet,10)
m2 = muvelet(gyok,100)
m3 = muvelet(math.sin, 5)
m4 = muvelet(math.cos, 4)
m5 = muvelet(math.tan, 3)
m6 = muvelet(lambda x: x*x*x, 10)

print(m1)
print(m2)
print(m3)
print(m4)
print(m5)
print(m6)
