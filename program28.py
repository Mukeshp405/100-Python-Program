# for else loop
print("For loop :- ")
for i in range(6):
    print(i)
    if i == 4:
        break
else:
    print("Sorry i is not found!!!")

# while else loop
print("While Loop :- ")
i = 0
while i < 6:
    i = i + 1
    print(i)
    if i == 4:
        break
else:
    print("Sorry i is not found!!!")

for x in range(5):
    print("Iteration no {} in for loop".format(x + 1))
else:
    print("else block in loop")
print("Out of loop")