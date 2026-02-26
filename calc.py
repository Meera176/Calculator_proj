def add(n1, n2):
    return n1 + n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
fur_proc=""
while(True):
    if(fur_proc=="n" or fur_proc=="" ):
        a = int(input("Whats your first number?"))
    else:
        a=res


    op = input("[+,-,*,/] Select one among these operations which you want to perform ")
    b = int(input("Whats your second number?"))
    if (op == "+"):
        res = add(a, b)
    elif (op == "-"):
        res = sub(a, b)
    elif (op == "*"):
        res = mul(a, b)
    elif (op == "/"):
        res = divide(a, b)
    print(f"Result of {a}{op}{b} is",res)
    fur_proc = input(
        f"Type'y' to continue with {res} as one of the operand and if not press 'n' for new calc and operands")
    if (fur_proc == "n"):
        continue