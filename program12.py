# Pyhton pattern program of Star
for i in range(1, 10):
    for j in range(1, i):
        print(i, end=" ")
    print()
# Pyhton pattern program of Integer
# Pyhton pattern program of Character
ascii_value = 65

for i in range(1, 10):
    alpha = chr(ascii_value)
    # for j in range(i, 1):
    #     print(end = " ")  
    for j in range(0, i):
        print(alpha,end = " ")
    
    ascii_value += 1
    print()