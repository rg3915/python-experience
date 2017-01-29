def factorial(n):
    total = 1

    for i in range(1, n + 1):
        total *= i
    
    return total


def test_factorial():
	assert factorial(0) == 1
	assert factorial(1) == 1
	assert factorial(3) == 6
	assert factorial(4) == 24
	assert factorial(5) == 120
