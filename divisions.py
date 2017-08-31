def divisions(n, divisor):
    c = 0
    
    if divisor > n:
        return 0
    
    while divisor <= n:
        n = n/divisor
        c += 1
    
    return c
