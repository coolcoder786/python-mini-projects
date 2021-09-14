height=float(input("enter your height in foot\n"))
height_meters=height*0.305
weight=int(input("enter your weight in kg\n"))
BMI=weight/height_meters**2  # bmi=weight/square of your height in meters
print("BMI -",BMI)

if BMI>25:
    print("you are over weight")

elif BMI<18:
    print("you are under weight")

else:
    print("you are FIT")
