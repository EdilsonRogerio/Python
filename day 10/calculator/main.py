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

# Square
def square(n1):
    return n1 ** 2
# Exponent
def exponent(n1, n2):
    return n1 ** n2

# Guarda as operações em um dicionário
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "**": square,
    "^": exponent
}

# Função que calcula a operação
def calculator():
    print(logo)
    print("Bem vindo a Calculadora!")
    print("Voce pode somar, subtrair, multiplicar e dividir")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    # Imprime as operações
    for symbol in operations:
        print(symbol)
    
    should_continue = True
    
    while should_continue:
        # Pergunta qual operação o usuário deseja fazer
        operation_symbol = input("Escolha uma operação: ")

        # Calcula a operação
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