name=input("enter your name\n")
year=int(input("in which year you were born?\n"))
present_year=int(input("enter the present year\n"))
agecalculate=input("do you want to calculate your age (yes/no)\n")

if agecalculate=="yes":
    print(name,"your age is",present_year-year)
elif agecalculate=="no":
    print("ok byee")
else:
    print("pls enter yes/no")

if year>present_year:
    print("dont fool me you are not born yet")

