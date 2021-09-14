# Health Management System
# 3 clients - krishna , rinki , kashyap
def getdate():
    import datetime
    return datetime.datetime.now()
import datetime
def gettime():
    return datetime.datetime.now()
def take(clients):
    if(clients)==1:
        c1=int(input("enter 1 for adding exercise and 2 for adding food\n"))
        if(c1==1):
            value=input("Type here\n")
            with open("krishna-ex.txt","a") as f:
                f.write(str([str(gettime())])+": "+value+"\n")
                print("successfully added")
        elif(c1==2):
            value=input("type here\n")
            with open("krishna-food.txt","a") as f:
                f.write(str([str(gettime())])+": "+value+"\n")
                print("successfully added")
    elif(clients==2):
        c1=int(input("enter 1 for adding exercise and 2 for adding food\n"))
        if(c1==1):
            value=input("type here\n")
            with open("rinki-ex.txt","a") as f:
                f.write(str([str(gettime())])+": "+value+"\n")
                print("successfully added")
        elif(c1==2):
            value=input("type here\n")
            with open("rinki-food.txt","a") as f:
                print("successfully added")

    elif(clients==3):
        c1=int(input("enter 1 for adding exercise and 2 for adding food\n"))
        if(c1==1):
            value=input("type here\n")
            with open("kashyap-ex.txt","a") as f:
                f.write(str([str(gettime())])+": "+value+"\n")
                print("successfully added")

        elif(c1==2):
            value=input("type here\n")
            with open("kashyap-food.txt","a") as f:
                f.write(str([str(gettime())])+": "+value+"\n")
                print("successfully added")

    else:
        print("pls enter a valid info (1 for krishna),(2 for rinki), (3 for kashyap)")

def retrive(clients):
    if clients==1:
        c1=int(input("enter 1 for exercise and 2 for food\n"))
        if(c1==1):
            with open("krishna-ex.txt") as f:
                for i in f:
                    print(i,end="")
        elif(c1==2):
            with open("krishna-food.txt") as f:
                for i in f:
                    print(i,end="")
    elif clients==2:
        c1 = int(input("enter 1 for exercise and 2 for food\n"))
        if(c1==1):
            with open("rinki-ex.txt") as f:
                for i in f:
                    print(i,end="")
        elif(c1==2):
            with open("rinki-food.txt") as f:
                for i in f:
                    print(i,end="")

    elif clients==3:
        c1 = int(input("enter 1 for exercise and 2 for food\n"))
        if c1==1:
            with open("kashyap-ex.txt") as f:
                for i in f:
                    print(i,end="")
        elif c1==2:
            with open("kashyap-food.txt") as f:
                for i in f:
                    print(i,end="")
    else:
        print("pls enter a valid info (1 for krishna),(2 for rinki), (3 for kashyap)")

print("HEALTH MANAGEMENT SOFTWARE")
a=int(input("press 1 for adding and 2 for retriving\n"))

if a==1:
    b=int(input("press 1 for krishna 2 for rinki and 3 for kashyap\n"))
    take(b)

if a==2:
    b = int(input("press 1 for krishna 2 for rinki and 3 for kashyap\n"))
    retrive(b)