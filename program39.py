# Write a Python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language.

# EnCoding.
# if the word contains atleast 3 characters, remove the fist letter and append it at the end, now append 3 random characters at the starting and the end.
# else:
#   simply reverse the string

# DeCoding.
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning.

st = str(input('Enter message :- '))
words = st.split(" ")
coding = input("1 for Coding and 0 for Decoding :- ")
coding = True if(coding == "1") else False

if(coding):
    nwords = []
    for word in words:
        if(len(word) >= 3):
            r1 = "dfa"
            r2 = "ged"
            stnew = r1 + word[1:] + word[0] + r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
else:
    nwords = []
    for word in words:
        if(len(word) >= 3):
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))