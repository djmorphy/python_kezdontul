# function decorators - fgv dekorator 2. resz
#pythonban minden objektum tehát a fgv is.

def validate_email(func):
    def wrapper(email,password):
        if "@" not in email:
            return "Not valid email!"
        return func(email, password)
    return wrapper


def validate_password(func):
    def wrapper(email, password):
        if len(password) < 6:
            return "Weak password at least 6 characters!"
        return func(email, password)
    return wrapper



@validate_email
@validate_password
def form(email,password):
    return "your pass is strong and you have valid email!"

print(form("attu","123457"))
print(form("attu@fwew.com","123457"))
print(form("attu@fwew.com","157"))
