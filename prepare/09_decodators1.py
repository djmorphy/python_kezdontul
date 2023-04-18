#function decorations - függvény dekoratorok
"""

    A dekorátor egy olyan tervezési mintázat a Python-ban amely lehetővé teszi a felhasználó
    számára hogy új funkcionalitást adjon egy meglévő objektumhoz anélkül hogy módosítaná annak struktúráját

a validate_div fogad egy függvényt a "func"-ot A divide függvény lesz a func bemenet.
A wrapper belső függvény becsomagolja a divide() függvényt-t

"""

#dekoralo fgv
def validate_div(func):
    def wrapper(value1, value2):
        if value2 == 0:
            return  "can not divide by zero"
        return func(value1,value2)
    return wrapper


""" 
ezzel dekorálom azaz ilyenkor hívja meg a string szöveget és nem a default hibaüzenetet kapom 
ha 0-val osztok
"""
#dekoralt fgv
@validate_div
def divide(value1,value2):
    return value1 / value2

print(divide(4,0))
print(divide(7,9))
print(divide(25,5))
print(divide(36,0))

#validate form
def validate_form(func):
    def wrapper(password, email):
        if len(password) < 6 :
            return "weak pass, at least 6 characters"
        if "@" not in email:
            return "not valid email"
        return func(password, email) # meghivjuk a dekoralt fgv
    return wrapper # visszaadjuk a csomagolt fgv

@validate_form
def form(passwrd, email):
    return "Your password is strong and you have valid email"

print(form("1234", "itere"))
print(form("1234567", "itere"))
print(form("123456", "itere@gmail.com"))

