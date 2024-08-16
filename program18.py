# ===== List method =====

# thislist = list(("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"))
# print(thislist[-1])
# print(thislist[len(thislist) - 1])
# print(thislist[-4:-3])
# print(thislist)

# thislist[1:3] = ["car"]
# print(thislist)

# ===== insert() method =====
# thislist.insert(2, "bus")
# print(thislist)

# ===== append() method =====
# thislist.append("apple")
# print(thislist)

# ===== extend() method =====
thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)

# tropical = ("kiwi", "orange")
# thislist.extend(tropical)

# print(thislist)

# ===== remove() method =====
# thislist.remove("apple")
# print(thislist)

# ===== pop() method =====
# thislist.pop(1)
# thislist.pop()
# print(thislist)

# ===== del keyword =====
# del thislist[0]
# print(thislist)

# del thislist

# ===== clear() method =====
# print(thislist)
# thislist.clear()
# print(thislist)

# ===== sort() method ====
# thislist.sort()
# thislist.sort(reverse=True)
# print(thislist)

# ===== reverse() method =====
# thislist.reverse()
# print(thislist)

# ===== copy() method =====
# print(thislist)
# mylist = thislist.copy()
# print(mylist)

#         OR (another method using list() method)

# ===== list() method =====
# print(thislist)
# mylist = list(thislist)
# print(thislist)

#          OR (another mehtod using (:) slice operator)

# ===== slice operator (:) =====
# print(thislist)
# mylist = thislist[:]
# print(mylist)

# ===== count() method ===== 
fruit = ["apple", "banana", "mango", "apple"]
# x = fruit.count("apple")
# print(x)

# ===== index() method =====
x = fruit.index("banana")
print(x)

