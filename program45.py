# Map, filter and reduce method

# ===== map method =====
# def cube(x):
#     return x * x * x

# print(cube(3))

# l = [1, 2, 3, 4, 6, 3, 4]
# # newl = []
# # for item in l:
# #     newl.append(cube(item))

# newl = list(map(cube, l))
# print(newl)

# ===== Filter method =====

# def filter_function(a):
#     return a > 2

# newnewl = list(filter(filter_function, l))
# print(newnewl)

# ===== Reduce mehtod =====

from functools import reduce

numbers = [1, 2, 3, 4, 5]

# def mysum(x, y):
#     return x + y

sum = reduce(lambda x, y: x + y, numbers)

print(sum)
