import random
print("NUMBER GUESSING GAME")
number=random.randint(0,100)
chance=0
numberOfChance=int(input("how many chances do you want"))
while chance<numberOfChance:
    user=int(input("enter any number between 0 and 100\n"))
    if user==number:
        print("you guesssed the right and took ",chance," chance to guess the right number")
        print("you won congrates")
        break
    elif user>number:
        print(f"please enter a less number then {user}")
        chance=chance + 1
    else:
        print(f"please enter a greater number then {user}")
        chance=chance + 1

if not chance<numberOfChance:
        print("you lost\nThe real number was",number)

        
