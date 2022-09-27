
import random
value=random.randint(1,100)


print("\n\n\n\n\t\t\t\t\t\t\t\t  ******** {GUESS THE NUMBER GAME} ******** ")

nam=' '
name=input("\n\n\n\t ENTER YOUR NAME ::: ")
nam=name.upper()
print("\n\n\t\t\t\t\t\t\t _____________________________________________________")
print("\n\t\t\t\t\t\t\t\t\t WELCOME {} TO OUR GAME ".format(nam))
print("\n\t\t\t\t\t\t\t _____________________________________________________")


print("\n\n\n\n\n\t\t\t\t\t\t\t\t    ** RULES OF PLAYING THE GAME **")
print("\n\t\t\t\t\t\t\t a)You must enter only valid integer with a range from \n\t\t\t\t\t\t\t   1 to 100.")
print("\n\t\t\t\t\t\t\t b)You will be provided 8 attempts to guess the number. ")
print("\n\t\t\t\t\t\t\t c)You cannot leave the game,once started. ")


for i in range(8):
    take=int(input("\n\n\n\n\n\n\t ENTER THE NUMBER: "))

    if take > value:
        print("\n\n\t NUMBER YOU GUESSED IS BIGGER THAN DESIRED NUMBER ")


    elif take < value:
        print("\n\n\t NUMBER YOU GUESSED IS SMALLER THAN DESIRED NUMBER ")


    else:
        print("\n\n\t EXCELLENT YOU GUESSED THE RIGHT NUMBER ")
        break

    
print("\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t  ******** THANKS FOR PLAYING ******** ") 
      
