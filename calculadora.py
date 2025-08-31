def soma(n1, n2):
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

def multiplicacao(n1, n2):
    return n1 * n2

def divisao(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "Erro: Divisão por zero não é permitida."

def porcentagem(n1, n2):
    if n2 != 0:
        return n1 * (n2 / 100)
    else:
        return "Erro: Porcentagem por zero não é permitida."


# Dicionário de operações
operacoes = {
    "+": soma,
    "-": subtracao,
    "*": multiplicacao,
    "/": divisao,
    "%": porcentagem
}

# Histórico
historico = []

while True:
    try:
        print("\nCalculadora Simples")
        print("Operações disponíveis: +, -, *, /, %")
        print("-----------------------------")
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operador = input("Digite a operação (+, -, *, /, %): ")
        
        if operador in operacoes:
            resultado = operacoes[operador](num1, num2)
            print(f"O resultado de {num1} {operador} {num2} é: {resultado:.2f}")
            historico.append(f"{num1} {operador} {num2} = {resultado:.2f}")
        else:
            print("Operação inválida. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Por favor, insira números válidos.")
    
    continuar = input("Deseja realizar outra operação? (s/n): ").lower()
    if continuar != 's':
        print("\nEncerrando a calculadora. Até mais!")
        print("\n📜 Histórico de operações:")
        for h in historico:
            print(h)
        break
