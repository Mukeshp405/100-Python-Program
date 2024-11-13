# Use of finally keyword

def func1():
    try:
        l = [1,2, 3, 4]
        i = int(input("Enter the number :- "))
        print(l[i])
        return 1
    except:
        print("Some error occured")
        return 0
    finally:
        print("I am always executed")

x = func1()
print(x)