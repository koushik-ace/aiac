def factorial_from_user():
    try:
        n = int(input("Enter a non-negative integer: "))
        if n < 0:
            print("Factorial is not defined for negative numbers.")
            return None
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    except ValueError:
        print("Invalid input. Please enter a non-negative integer.")
        return None

output = factorial_from_user()
if output is not None:
    print(f"The factorial is {output}")

