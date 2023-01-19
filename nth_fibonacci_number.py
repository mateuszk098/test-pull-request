"""
Calculate nth-fibonacci number.
"""

def nth_fibonacci(n):
    "Return nth-fibonacci number."
    if n < 0:
        raise ValueError("The `n` attribute should be >= 0.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    numbers = [0] * (n + 1)
    numbers[1] = 1
    for i in range(2, n + 1):
        numbers[i] = numbers[i-2] + numbers[i-1]
    
    return numbers[-1]

assert nth_fibonacci(0) == 0
assert nth_fibonacci(5) == 5
assert nth_fibonacci(13) == 233