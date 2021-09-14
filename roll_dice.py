import random
minimum=1
maximum=6

i="yes"
while i=="yes":
    print("rolling the dice......\nrolling the dice....")
    print("the numbers are")
    print(random.randint(minimum,maximum))
    print(random.randint(minimum,maximum))

    i=input("want to roll the dice again?")