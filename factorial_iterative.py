def factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return None if n < 0 else f
