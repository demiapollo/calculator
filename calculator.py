from art import logo

## Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

# Defining a dic with operations as keys & names of the functions as values
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))
    for operation in operations:
        print(operation)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        function = operations[operation_symbol]
        answer = function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        question_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if question_continue == 'y':
            num1 = answer
        elif question_continue == 'n':
            should_continue = False
            calculator()

calculator()