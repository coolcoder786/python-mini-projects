import random
move=["rock","paper","scissor"]
chances=int(input("how many chances do you want to play\n"))
no_of_chance=0
palyer_points=0
comp_points=0

print("hello lets play a game and that is ROCK/PAPER/SCISSOR game")

while no_of_chance < chances:
    user=input("choose 1\n'r' for rock\n'p' for paper\n's' for scissor\n")
    comp=random.choice(move)

    if user==comp:
        print("computer also choosed",comp)
        print("game tied")
        
    elif user=="r" and comp=="paper":
        print("computr choosed",comp)
        print("computer won")
        comp_points=comp_points+1

    elif user=="p" and comp=="rock":
        print("computr choosed",comp)
        print("you won")
        palyer_points=palyer_points+1

    elif user=="r" and comp=="scissor":
        print("computr choosed",comp)
        print("you won")
        palyer_points=palyer_points+1

    elif user=="s" and comp=="rock":
        print("computr choosed",comp)
        print("computer won")
        comp_points=comp_points+1

    elif user=="p" and comp=="scissor":
        print("computr choosed",comp)
        print("computer won")
        comp_points=comp_points+1

    elif user=="s" and comp=="paper":
        print("computr choosed",comp)
        print("you won")
        palyer_points=palyer_points+1

    else:
        print("INVALID INPUT")
    
    no_of_chance=no_of_chance+1
    print(chances-no_of_chance,"chances left out of",chances)

print("game over")
if comp_points==palyer_points:
     print("game ended with a TIE")
elif comp_points>palyer_points:
    print("computer have more points then you so computer won")
else:
    print("you have more points then computer so you won")

print("your points are",palyer_points,"and computer points are",comp_points)
