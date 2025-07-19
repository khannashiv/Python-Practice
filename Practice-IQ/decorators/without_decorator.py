def my_dec(func):
    def wrapper():
        print("Print something before the actual function.")
        func()
        print("Print something after the actual function. ")
    return wrapper


def say_hello():
    print("Hello & hi !!")

# M1 : Where we are storing the outcomes in new variable

# decorated_func = my_dec(say_hello)
# decorated_func()

# M2

say_hello = my_dec(say_hello)
say_hello()