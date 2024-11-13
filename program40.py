# File Handling

# READING a file
# f = open("myfile.txt", 'w')
# text = f.write()
# print(text)
# f.close()

# WRITING a file
f = open("myfile2.txt", 'w')
f.write("Hello world")
f.close()

with open("myfile.txt", 'w') as f:
    f.write("Hey I am inside with!")