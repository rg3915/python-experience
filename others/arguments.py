def soma(**kwargs):
    return sum(kwargs.values())


if __name__ == '__main__':
    d = {
        'a': 20,
        'b': 2,
        'c': 12,
        'd': 8,
    }
    print(soma(**d))