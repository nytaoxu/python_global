zeros = [0] * 10
print(zeros)
matrix = [[1, 2], [3, 4]]
print(matrix)
print(matrix[0])
print(matrix[1][1])
print(type(matrix))
combined = zeros + matrix
print(combined)
print(zeros, matrix)
numbers = list(range(10))
print(numbers)
chars = list("Hello World")
print(chars)
print(chars[0:])
print(chars[:-1])
print(chars[::2])
print(list(range(20)))
x, y, *z = chars
print(x, y, z)
print(type(z))
x, *y, z = chars
print(x, y, z)
