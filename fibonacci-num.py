def fibonacci_sum(n):
    a, b = 0, 1
    fib_sum = 0
    for _ in range(n):
        fib_sum += a
        a, b = b, a + b
    return fib_sum

if __name__ == "__main__":
    fib_sum = fibonacci_sum(50)
    print("Sum of first 50 Fibonacci numbers:", fib_sum)

