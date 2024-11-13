# OS Module
import os

# Make Directory
# if(not os.path.exists("data")):
#     os.mkdir("data")

# for i in range(0, 100):
#     os.mkdir(f"data/Day{i+1}")

# Rename Directory

# for i in range(0, 100):
#     os.rename(f"data/Tutorial {i+1}", f"data/Tutorial{i+1}")

# oslist

folders = os.listdir("data")

print(os.getcwd())
# os.chdir("/laptop")
# print(os.getcwd())

for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}"))