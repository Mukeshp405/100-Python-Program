# String Methods

# Strings are immutable
name = "!!!Mukesh !!!!!!!!! Mukesh"

# len()
print('Length :- ',len(name))

# upper()
print('UpperCase :- ', name.upper())

# lower()
print('LowerCase :- ', name.lower())

# strip()
print('Strip :- ', name.strip("!"))

# rstrip()
print('Rstript :- ', name.rstrip("!"))

# lstrip()
print('Lstript :- ', name.lstrip("!"))

# replace()
print('Replace :- ', name.replace('Mukesh', 'John'))

# split()
print('Split :- ', name.split(" "))

# capitalize()
blogHeading = "introduction to js"
print(blogHeading.capitalize())

# center()
str1 = "Welcome to the Console!!!"
print(len(str1))
print(len(str1.center(50)))
print(str1.center(100))

# count()
print(name.count("Mukesh"))

# startswith()
print(str1.startswith("Mukesh"))

# endswith()
print(str1.endswith("!!!"))
print(str1.endswith("to", 4, 10))

# find()
str1 = "He's name is Dan. He is an honest man."
print("Find :-", str1.find("is"))

# index()
# print("Index :-", str1.index('ishh'))

# isalnum() :- is string alpha numeric (A-Z, a-z, 0-9)
str1 = "WelcomeToTheConsole123"
print("is string Alpha numeric :-", str1.isalnum())

# isalpha() :- is string contain only alphabate (A-Z, a-z)
print("is string contain only alphabate :- ", str1.isalpha())

# islower()
print("is Lower :-", str1.islower())

# isupper()
print("is upper :-", str1.isupper())

# isprintable()
str1 = "This is the printable method\n"
print("is printable :-", str1.isprintable())

# swapcase()
print("SwapCase :- ", str1.swapcase())

# title()
print("Title :-", str1.title())

# isspace()
print("is space :-", str1.isspace())

# istitle()
print("is title :-", str1.istitle())

# casefold()
print("Casefold :- ", str1.casefold())

# encode()
print("Encode :- ", str1.encode())

# expandtabs()
print("Expandtabs :- ", str1.expandtabs(2))

# F-String
age = 36
txt = f"My name is Mukesh, I am {age}"
print(txt)

price = 59
text = f"The price is {price:.5f} dollars"
print(text)

text = f"The price is {20 + 30} dollars"
print(text)

# String Concatenation
a = "Hello"
b = "World"
c = a + " " + b
print(c)


print(bool(0))