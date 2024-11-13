# Classes and Object 

# Class created 
# class Person:
#     name = "Dhiraj"
#     occupation = "Animation Creator"
#     networth = 10
#     def info(self):
#         print(f"{self.name} is a {self.occupation}")

# # Object Created
# a = Person()
# b = Person()
# c = Person()

# a.name = "Shubham"
# a.occupation = "Accountant"

# b.name = "Nitika"
# b.occupation = "Web Developer"

# a.info()
# b.info()
# c.info()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Jhon", 36)

print(p1.name)
print(p1.age)