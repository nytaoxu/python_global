letters = ['a', 'b', 'c', 'c']

# find
if 'd' in letters:
    print(letters.index('d'))

if letters.count('c') > 0:
    print(letters.index('c'))

letters.sort(reverse=True)
print(sorted(letters, reverse=True))
print(letters)
print(len(letters))

items = [
    ('a', 3),
    ('b', 2),
    ('c', 1)
]


def sort_item(item):
    return item[1]


print("items =", items)
# items.sort(key=sort_item)
# items.sort(key=lambda prarmeters:expression)
items.sort(key=lambda item: item[0], reverse=True)
print("itmes =", items)
