#closures - bezárások
# a külső fgv lefut de a belső fgv még mindig megjegyezte a változót és referál rá tudja használni

def kulso ():
    szam = 21
    def belso():
        """ szam += 1 ez nem működik mert nonlocal-t kell használjak"""
        nonlocal szam
        szam += 1
        print(szam)  #belo fgv nem tudom módosítani a számot de tudom használni. Modosítani a nonlocal-al lehet
    return belso

f1 = kulso()
f1()
