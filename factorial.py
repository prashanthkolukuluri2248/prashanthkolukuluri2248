def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
try:
    n = int(input("Enter a  integer: "))

    result = factorial(n)
    print(f"The factorial of {n} is: {result}")
except ValueError as e:
    print(f"Error: {e}")




