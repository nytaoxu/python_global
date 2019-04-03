numbers = [1, 2, 3]
print(numbers)
print(1, 2, 3)
print((1, 2, 3))
print(*numbers)

print(list(range(5)))
print([*range(5), *"abcxyz"])

first = {"x": 1}
second = {"x": 2, "y": 3}
combined = {**first, **second}
print(combined)
print({**second, **first})

# from sys import getsizeof

# values = []
# for item in range(5):
#     values.append(item * 2)
# print(values)

# values_alt = [2 * item for item in range(5)]
# print(values_alt)

# values_set = {2 * item for item in range(5)}
# print(values_set)

# values_dict = {item: item * 2 for item in range(5)}
# print(values_dict)

# values_generator = (item for item in range(50000))
# print(values_generator)
# print(getsizeof(values_generator))
# print(len(values_generator))

# point = {"x": 5, 'y': 7}
# print(point)
# point_alt = dict(x=5, y=7)
# print(point_alt)
# # print(point.x)
# print(point["y"])
# if 'a' in point:
#     print(point['a'])
# else:
#     print("No 'a' key.")
# print(point.get('a', 57))
# print(point)
# del(point['x'])
# print(point)
# point['z'] = 57
# for i in point:
#     print(i, point[i])
# for j in point.items():
#     print(type(j))
#     print(j)
# for key, value in point.items():
#     print(key, value)
