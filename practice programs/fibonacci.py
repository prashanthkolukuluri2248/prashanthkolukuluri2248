def fibonacci(x):
    n = [0, 1]
    for i in range(2, x):
        next_fib = n[-1] + n[-2]
        n.append(next_fib)
    return n
num_terms = 10
print(f"Fibonacci series (up to {num_terms} terms): {fibonacci(num_terms)}")
