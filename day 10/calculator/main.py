from art import logo

print(logo)

# Add
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

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    for symbol in operations:
        print(symbol)
    should_continue = True
    
    while should_continue:
        operation_symbol = input("Escolha uma operação: ")

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        continue_calculation = input(f"Você quer continuar calculando com {answer}? Digite 's' para sim ou 'n' para não: ")
        if continue_calculation == "s":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()