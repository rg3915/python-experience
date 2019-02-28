def my_decorator(func):
    def wrapper():
        print('Before')
        func()
        print('After')
    return wrapper


def say_whee():
    print('Whee')


say_whee = my_decorator(say_whee)


if __name__ == '__main__':
    say_whee()