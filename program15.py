# Function in Python

def calculateGmean(a, b):
    mean = (a * b)/(a + b)
    print(mean)

def isGreater(a, b):
    if(a > b):
        print("First Number is gretere")
    else:
        print("Second Number is greater or equal")

a = 9
b = 8
isGreater(a, b)
calculateGmean(a, b)