items = [
    ("Product 1", 10),
    ('Product 2', 9),
    ("Product 3", 12)
]

prices = []
for item in items:
    prices.append(item[1])

new_items = map(lambda item: item[1], items)

u = list(new_items)

print(prices)
print(new_items)

for x in new_items:
    print(x)
prices = list(new_items)
print(prices)
print(u)

filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)

# comprehension
# [expression] for item in items
prices_alt = [item[1] for item in items]
print(prices_alt)

filtered_alt = [item for item in items if item[1] >= 10]
print(filtered_alt)
