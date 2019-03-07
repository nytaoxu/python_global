letters = ('x', "y", 'z')  # ['a', "b", 'c']
for letter in enumerate(letters):
    print(letter, letter[0], letter[1])
for index, letter in enumerate(letters):
    print(index, letter)
x = [1, 2]
x1, x2 = x
print(x, x1, x2)
y = (3, 4)
y1, y2 = y
print(y, y1, y2)
