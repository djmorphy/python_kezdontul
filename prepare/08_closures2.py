#closures - bezarasok 2. resz
# operator factory closure function
#valszeg ritkan hasznalok majd ilyet

def op_factory(oper, num):
    def operation(value):
        if oper == "**":
            return value ** num
        elif oper == "*":
            return  value * num
        elif oper == "/":
            return value / num
        else:
            return "not supported operator!"

    return  operation

negyzet  = op_factory("**",2)
kob = op_factory("**", 3)

print(negyzet(5))
print(kob(5))

test1 = op_factory("$", 3)
print(test1(5))

mult4 = op_factory("*", 4)
print(mult4(8))

div_by_5 = op_factory("/", 5)
print(div_by_5(45))