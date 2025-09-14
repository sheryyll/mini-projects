from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Error: Cannot divide by zero"
    return n1 / n2

operators = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    should_accumulate = True

    while should_accumulate:
        print("Available operations:")
        for symbol in operators:
            print(symbol)

        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        answer = operators[operation_symbol](num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(
            f"Type 'y' to continue with {answer}, 'n' to start new, or 'q' to quit: "
        )

        if choice == 'y':
            num1 = answer
        elif choice == 'n':
            calculator()               
            should_accumulate = False  
        else:  # 'q'
            print("Goodbye ")
            should_accumulate = False  

calculator()
