#  Print Fibonacci Series


def fibonacci(n):
    fib_series = []
    if n <= 0:
        return fib_series
    elif n == 1:
        fib_series.append(0)
        return fib_series
    elif n == 2:
        fib_series.extend([0, 1])
        return fib_series
    else:
        fib_series.extend([0, 1])
        a, b = 0, 1
        for _ in range(2, n):
            c = a + b
            fib_series.append(c)
            a, b = b, c
        return fib_series

# Test the function
num_terms = 10  # Change this value to generate Fibonacci series up to a different number of terms
fibonacci_series = fibonacci(num_terms)
print("Fibonacci series up to", num_terms, "terms:", fibonacci_series)
