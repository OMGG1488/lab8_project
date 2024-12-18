def find_min_positive(arr):
    return min(arr)

def sum_negative(arr):
    return sum(arr)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def electric_current(voltage, resistance):
    return voltage / resistance
