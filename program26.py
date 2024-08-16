info = {
    'name': 'Karan',
    'age':19,
    'eligible': True
}

# print(info)
# print(info['name2'])
# print(info.get('name2'))

# To print all keys
# print(info.keys())
# print(info.values ())

# for key in info.keys():
#     print(f"The value corresponding to the key {key} is {info[key]}")

print(info.items())

for key, value in info.items():
    print(f"The value corresponding to the key {key} is {value}")
    