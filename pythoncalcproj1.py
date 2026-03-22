def add(x, y):
        """Return the sum of two numbers."""
        return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
while True:
    # Placeholder for calculator operations
    # e.g., get user input(), eval(), etc., print() results, etc.
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Enter operation (+, -, *, /): ")
        if operation == '+':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif operation == '-':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif operation == '*':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif operation == '/':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        else:
            print("Invalid operation. Please try again.")
    except ValueError:
        print("Invalid input. Please enter numeric values.")
