# Recursion in python

# Factorial using recursion
# Formula :- factorial(n) = n * factorial(n-1)
# def factorial(n):
#     if(n == 0 or n == 1):
#         return 1
#     else:
#         return n * factorial(n - 1)

# print(factorial(5))



# Fibonacci series using recursion
# f(0) = 0
# f(1) = 1
# f(2) = f(1) + f(0)
# f(n) = f(n-1) + f(n-2)
# 0 1 1 2 3 5 8 13...

def fibonacci(n):
    if(n < 0):
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_series(lenght):
    series=[]
    for i in range(lenght):
        series.append(fibonacci(i))
    return series

if __name__ == "__main__":
    length = int(input("Enter the numbr of fibonacci numbres to generate :- "))
    print("Fibonacci series :- ")
    print(fibonacci_series(length))
