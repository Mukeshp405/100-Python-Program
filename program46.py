# Snake, Water and Gun game

from random import *

print()
print("----------------------------")
print("\tChoose one :")
print("\t0. Snake")
print("\t1. Water")
print("\t2. Gun")
print("----------------------------")
print()

choose = int(input("Choose one number :- "))
print()
print("----------------------------")

# User number function
def choose_number(choose):
    if choose >= 0 and choose <= 2:
        if choose == 0:
            print("You choose :- Snake")
        elif choose == 1:
            print("You choose :- Water")
        else:
            print("You choose :- Gun")
    else:
        print("Invalid number!!!")
        print("----------------------------")
        exit()


# Random number function
random_choose = randint(0, 2)
def random_number_choose():
    if random_choose == 0:
        print("Computer choose :- Snake")
    elif random_choose == 1:
        print("Computer choose :- Water")
    else:
        print("Computer choose :- Gun")
    
    print("----------------------------")

# Result (Win or Lose)
def win_lose():
    print("----------------------------")
    if choose == random_choose:
        print("\tDraw Match!!!")
    elif choose == 0 and random_choose == 1:
        print("\tYou Win!!!")
    elif choose == 1 and random_choose == 2:
        print("\tYou Win!!!")
    elif choose == 2 and random_choose == 0:
        print("\tYou Win!!!")
    else:
        print("\tYou Lose!!!")
    print("----------------------------")
    

# Main function
def main():
    choose_number(choose)
    random_number_choose()
    win_lose()

main()