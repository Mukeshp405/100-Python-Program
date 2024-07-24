# Create a pyhton program capable of greeding you with Good Morning, Good Afternoon and Good Evening. Your program should use time module to get the 
# current hour. Here is a sample program and documentation link for you.

import time

timestamp = time.strftime('%H:%M:%S')
print(timestamp)

timestamp = int(time.strftime('%H'))
# print(timestamp)
if(timestamp < 12):
    print("Good Morning!!!")
elif(timestamp > 12 and timestamp < 16):
    print("Good Afternoon!!!")
else:
    print("Good Evening!!!")

# timestamp = time.strftime('%M')
# print(timestamp)

# timestamp = time.strftime('%S')
# print(timestamp)