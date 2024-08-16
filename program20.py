# ===== Tuples in Pyhton =====
tup1 = (1,2, 76, 342, 32, "green", True)
# print(tup1)

tup2 = tuple(("apple", "banana", "mango"))
# print(tup2)

# ===== Change Tuple Values =====
# print(tup2)
# y = list(tup2)
# y[1] = "kiwi"
# tup2 = tuple(y)
# print(tup2)

# ===== Add tuple =====
# tup3 = ("orange",)
# tup2 += tup3
# print(tup2)


fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)