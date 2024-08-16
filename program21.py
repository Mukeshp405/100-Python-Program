# Create a python program capable of displaying questions to the user like KBC.
# Use List data type to store the questions and their correct answer.
# Display the final amount the person is taking home playing the game.

name = str(input("Enter your name :- "))
age = int(input("Enter your age :- "))

print()
print("------- User Info -------")
print("Your name is :-", name)
print("Your age is :-", age)
print("-------------------------")

def gameOver():
    print("Thanks for playing the game!!!")

def KBC():
    print()
    print("Your question is :- ")

    # Question 1
    def q1():
        print()
        print("1. In which state is Varkala Beach situated?")
        print("a. Maharashtra")
        print("b. Rajasthan")
        print("c. Kerala")
        print("d. Bihar")

        ans = str(input("Choose :- "))
        if ans == "c":
            print("*** You win ***")
            q2()
        elif ans == 'a' or ans == 'b' or ans == 'd':
            print("--- You Lose ---")
            q1()
            choice = str(input("Do you want to continue(y/n) :- "))
            if choice == 'y':
                q2()
            elif choice == 'n':
                gameOver()                
            else:
                print("Invalid input!!!")
        else:
            print("Invalid input!!!")
            q1()
    
    # Question 2
    def q2():
        print()
        print("2. Which animal is known as the 'Ship of the Desert'?")
        print("a. Camel")
        print("b. Lion")
        print("c. Horse")
        print("d. Elephant")

        ans = str(input("Choose :- "))
        if ans == 'a':
            print("*** You win ***")
            print()
        elif ans == 'b' or ans == 'c' or ans == 'd':
            print("--- You Lose ---")
            q2()
            choice = str(input("Do you want to continue(y/n) :- "))
            if choice == 'y':
                # q3() 
                print("hello")
            elif choice == 'n':
                print("Thanks for playing the game!!!")
                
            else:
                print("Invalid input!!!")
        else:
            print("Invalid input!!!")
            q2()

    # Question 3
    # Question 4
    # Question 5

    q1()
    
KBC()
