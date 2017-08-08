def soma(**kwargs):
    result = [kwargs[i] for i in kwargs]
    return sum(result)


if __name__ == '__main__':
    d = {
        'a': 20,
        'b': 2,
        'c': 12,
        'd': 8,
    }
    print(soma(**d))