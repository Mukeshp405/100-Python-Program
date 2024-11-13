# Enumerate function

marks = [33, 54, 67, 78, 34, 56, 45]

# index = 0
for index, mark in enumerate(marks, start=1):
    if(index == 3):
        print("replace")
    print(mark)
    # index =+ 1