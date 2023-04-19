import time
#3-as begyazas lesz.
# a validate_form vissza adja a wrappert a main_decorator vissza adja a validate_form-ot



def main_decorator(state):
    def validate_form(func):
        def wrapper(password, email):
            print(state)
            time.sleep(5)
            if len(password) < 6:
                return "weak pass, at least 6 characters"
            if "@" not in email:
                return "not valid email"
            return func(password, email)
        return wrapper
    return validate_form

@main_decorator("validateing.......")
def form(password, email):
    return "Your password is strong and you have valid email"

print(form("1234", "itere"))
print(form("1234567", "itere"))