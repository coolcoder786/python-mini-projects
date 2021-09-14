def add(a,b):
    return a+b

def sub(a,b):
   return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

a=float(input("enter first number\n"))
b=float(input("enter second number\n"))

choice=int(input("1 for addition 2 for substraction 3 for multiplication and 4 for multiplication\n"))

if choice==1:
    print(add(a,b))

elif choice==2:
    print(sub(a,b))

elif choice==3:
    print(mul(a,b))

elif choice==4:
    print(div(a,b))

else:
    print("invalid input")
