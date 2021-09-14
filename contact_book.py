print("WELCOME TO MY CONTACT BOOK , YOU CAN ADD ANY ONE IN THIS LIST\n")

want = input("Do you want to add contacts  or show contactrs , for adding press 'add' \n for showing press 'a' ")
            
if want=="add":
      firstName=str(input("enter first name "))
      lastName=str(input("enter Last name "))
      num = int(input("Enter his/her Number "))
      print(firstName+" "+lastName+":"+str(num))

      user = input("1. for saving press 's'\n2. for adding more contacts press 'y' ")
      while user=="y":
            firstName=str(input("enter first name "))
            lastName=str(input("enter Last name "))
            num = int(input("Enter his/her Number "))
            print(firstName+" "+lastName+" "+str(num))
            user = input("1. for saving press 's'\n2. for adding more contacts press 'y' ")

      if user=="s":
            with open("numbers.txt","a") as f:
                  f.write(firstName+" "+lastName+":"+str(num)+"\n")
                  print("NUMBER IS SUCCESFULLY SAVED")

      while user=="n":
            print("Thanks for using my contact book")
            break

                  
if want=="a":
      with open("numbers.txt","r") as f:
            data=f.read()
            print(data)
            


