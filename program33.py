# Write a Python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language.

# EnCoding.
# if the word contains atleast 3 characters, remove the fist letter and append it at the end, now append 3 random characters at the starting and the end.
# else:
#   simply reverse the string

# DeCoding.
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning.

import string
import random

message = str(input("Enter your message here :- "))

# EnCoding
if len(message) >= 3:
    for i in range(3):
        app = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
        print(app, end="")

    mess = message[0]
    message = message.replace(mess, '') + mess
    print(message,end="")

    for i in range(3):
        app = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
        print(app, end="")
else:
    str = ""
    for i in message:
        str = i + str
    print(str)

# Decoding

# if len(message) < 3:
#     str = ""
#     for i in message:
#         str = i + str
#     print(str)
# else:
#     for i in range(3):
#         app = message.replace(message[i], '')
#         # print(message.replace(message[i], ''))
#     print(app)
        # app = message.replace(app[0, 1, 2], '')
        # print(app, end="")