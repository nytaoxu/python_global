def save_user(**user):
    print(user)
    for x in user:
        print(x, user[x])


save_user(a=1, b=2, c='xyz')
message = "a"


def greet(name):
    message = "b"


def greet2(name):
    global message
    message = "c"


greet("Tao")
print("message =", message)
greet2("Xu")
print("message =", message)
