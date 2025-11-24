def fibonacci_series(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

n = int(input("Enter the number of terms for the Fibonacci series: "))
fib_series = fibonacci_series(n)
print(f"Fibonacci series of {n} terms:", fib_series)