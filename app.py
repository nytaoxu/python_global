def multiply(*numbers):
    product = 1
    for number in numbers:
        product *= number
    return product


print("Start...")
print(multiply(1, 2, 3))
