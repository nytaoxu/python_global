def multiply(*numbers):
    product = 1
    for number in numbers:
        product *= number
    return product


print("Start...")
print(multiply(1, 2, 3))


def fizz_buzz(number):
    if number % 15 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number


print(fizz_buzz(16))
