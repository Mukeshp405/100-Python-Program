# seek() and tell() method
# with open("myfile.txt", 'r') as f:
#     # print(type(f))
#     f.seek(10)

#     print(f.tell())
#     data = f.read(5)
#     print(data)

# truncate() method
with open("myfile5.txt", 'w') as f:
    f.write("Hello world!")
    f.truncate(5)

with open("myfile5.txt", 'r') as f:
    data = f.read()
    print(data)
    f.close()