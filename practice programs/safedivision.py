try:
    x=int(input("Enter first number: "))
    y=int(input("Enter second number:"))
    result = x%y
except ValueError:
    print("Input not valid ,Enter an valid input: ")
except ZeroDivisionError:
    print("Zero is not divisible,Enter an valid input: ")
else:
    print(result)
