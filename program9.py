# Create a pyhton program capable of greeding you with Good Morning, Good Afternoon and Good Evening. Your program should use time module to get the 
# current hour. Here is a sample program and documentation link for you.

import time

timestamp = time.strftime('%H:%M:%S')
print(timestamp)

hour = int(time.strftime('%H'))
# hour = int(input("Enter the hour: "))
# print(hour)

if(hour >= 0 and hour < 12):
    print("Good Morning!!!")
elif(hour >= 12 and hour < 17):
    print("Good Afternoon!!!")
elif(hour >= 17 and hour < 0):
    print("Good Night!!!")
else:
    print("Enter the valid hour!!!")