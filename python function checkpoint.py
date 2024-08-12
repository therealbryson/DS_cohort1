# Basic mathematical functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

# Dictionary mapping operation symbols to functions
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

# Calculator function
def calculator():
    num1 = float(input("Enter the first number: "))

    while True:
        print("Available operations: +, -, *, /")
        operation = input("Choose an operation symbol (+, -, *, /) or 'q' to quit: ")

        if operation == 'q':
            print("Exiting calculator.")
            break
        
        if operation not in operations:
            print("Invalid operation symbol. Please choose from +, -, *, / or 'q' to quit.")
            continue
        
        num2 = float(input("Enter the second number: "))
        calculation_function = operations[operation]
        answer = calculation_function(num1, num2)
        
        print(f"{num1} {operation} {num2} = {answer}")
        
        should_continue = input(f"Use {answer} as the first number for the next calculation? (y/n): ").strip().lower()
        
        if should_continue == 'y':
            num1 = answer
        else:
            print("Starting a new calculation.")
            calculator()

# Starting the calculator
calculator()
