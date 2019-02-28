def my_decorator(func):
    def wrapper():
        print('Before')
        func()
        print('After')
    return wrapper


@my_decorator
def say_whee():
    print('Whee')


if __name__ == '__main__':
    say_whee()
