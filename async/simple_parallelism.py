from multiprocessing.dummy import Pool as ThreadPool


def square_number(n):
    return n ** 2


def calculate_parallel(numbers, threads=2):
    pool = ThreadPool(threads)
    results = pool.map(square_number, numbers)
    pool.close()
    pool.join()
    return results


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    square_numbers = calculate_parallel(numbers, 4)
    for n in square_numbers:
        print(n)
