point = {"x": 5, 'y': 7}
print(point)
point_alt = dict(x=5, y=7)
print(point_alt)
# print(point.x)
print(point["y"])
if 'a' in point:
    print(point['a'])
else:
    print("No 'a' key.")
print(point.get('a', 57))
print(point)
del(point['x'])
print(point)
point['z'] = 57
for i in point:
    print(i, point[i])
for j in point.items():
    print(type(j))
    print(j)
for key, value in point.items():
    print(key, value)
