# Function Arguments and return statement in Python
    #  There are four types of arguments that we can provide in a function

#  1. Default Arguments
# print("============ Default Argument ============")
# def average(a = 9, b = 1):
#     print("The average is: ", (a+b)/2)

# average(b = 9)

# def name(fname, mname = "Jhon", lname = "Whatson"):
#     print("Hello,", fname, mname, lname)

# name("Amy", "Agarwal", "Jain")

# #  2. Keyword Arguments
# print("============ Keyword Argument ============")
# def average2(a, b = 1):
#     print("The average is: ", (a + b)/2)

# average2(b = 2, a = 21)

#  3. Variable length Arguments
print("============ Variable Length Argument ============")
def average4(*numbers):
    # print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is: ", sum / len(numbers))

average4(5, 6, 7, 1)

#  4. Required Argumnets
# print("============ Required Arguments ============")
# def average3(a, b, c  = 1):
#     print("The average is: ", (a + b + c)/2)

# average3(5, 6)
