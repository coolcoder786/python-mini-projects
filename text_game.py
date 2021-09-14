print("WELCOME to my game")
name=input("what is your name\n")
print("hello", name)
health=10
age=int(input("what is your age\n"))
if age >= 10:
    print("you are old enough to play this game")
    wants_to_play=input("do you want to play the game\n")
    if wants_to_play=="yes":
        print("you have" ,health ,"health")
        print("lets paly")
        left_right=input("choose any one path 'left' or 'right' ")
        if left_right=="left":
            ans=input("nice ..you choosed the right path and now reached a river..Do you want to swim across the river or wants to go around the river (across/around)?\n")
            if ans=="around":
                print("you crossed the river and reached the other side of the lake")
            elif ans=="across":
                print("you were beaten by a fish and lost your 5 health")
                health -=5

            ans=input("you noticed a house and a river where do you want to go (house/river)?\n")
            if ans=="house":
                print("the owner of the house did not like you and beaten so you lost  5 health")
                health -=5

                if health<=0:
                    print("you now have 0 health so, you lost")
                else:
                    print("you survived till last without loosing your total helth so, you won")

            else:
                print("you fell in the river and lost")


        else:
             print("you choosed right but its the wrong path so you lost")


    else:
        print("ok bye bhag b***")
else:
    print("you are not old enouh to play this game")