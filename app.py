numbers = [1, 1, 1, 2, 3, 3, 4, 5]
first = set(numbers)
second = set([1, 3, 7, 8, 9])
print(first, second)
print(first | second)
print(first & second)
print(first - second)
print(first ^ second)

x = set([])
print(type(x))
x.add(1)
x.add(1.0)
x.add('1.0')
x.add('1')
print(x)
x.remove(1.0)
print(x)
for item in x:
    print(item)
