import math
import cmath

# Função para divisão complexa
def complex_division(z1, z2):
    try:
        result = z1 / z2
        return result
    except ZeroDivisionError:
        return "Divisão por zero não permitida no domínio quântico."

# Função para cálculo do logaritmo complexo
def quantum_logarithm(z):
    if z == 0:
        raise ValueError("Logaritmo indefinido para zero.")
    magnitude = abs(z)
    phase = cmath.phase(z)
    return complex(math.log(magnitude), phase)

# Função para calcular o fatorial
def factorial_performance(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_performance(n - 1)

# Função para cálculo da entropia quântica
def quantum_entropy(probabilities):
    entropy = 0
    for p in probabilities:
        if p > 0:
            entropy -= p * math.log2(p)
    return entropy

# Função principal com entradas dinâmicas
def dynamic_quantum_demo():
    print("===== MECÂNICA QUÂNTICA: DEMONSTRAÇÃO DINÂMICA =====")
    
    # Entrada de números complexos
    real_part = float(input("Digite a parte real de um número complexo: "))
    imag_part = float(input("Digite a parte imaginária de um número complexo: "))
    quantum_input = complex(real_part, imag_part)
    
    # Outro número complexo para divisão
    real_divisor = float(input("Digite a parte real do divisor complexo: "))
    imag_divisor = float(input("Digite a parte imaginária do divisor complexo: "))
    divisor = complex(real_divisor, imag_divisor)
    
    # Cálculo da divisão complexa
    division_result = complex_division(quantum_input, divisor)
    print(f"Divisão Complexa: {quantum_input} / {divisor} = {division_result}")
    
    # Cálculo do logaritmo complexo
    try:
        log_result = quantum_logarithm(quantum_input)
        print(f"Logaritmo Complexo: log({quantum_input}) = {log_result}")
    except ValueError as e:
        print(e)
    
    # Entrada para o fatorial
    n = int(input("Digite um número inteiro para o cálculo do fatorial: "))
    factorial_result = factorial_performance(n)
    print(f"Fatorial de {n}: {factorial_result}")
    
    # Entrada para probabilidades quânticas
    num_probabilities = int(input("Digite o número de estados quânticos (probabilidades): "))
    probabilities = []
    print("Digite as probabilidades (deve somar 1):")
    for _ in range(num_probabilities):
        p = float(input("Probabilidade: "))
        probabilities.append(p)
    
    # Verificar soma das probabilidades
    if not math.isclose(sum(probabilities), 1.0):
        print("Erro: as probabilidades devem somar 1. Encerrando.")
        return
    
    # Cálculo da entropia quântica
    entropy_result = quantum_entropy(probabilities)
    print(f"Entropia Quântica: {entropy_result} bits")
    
    print("\n--- DEMONSTRAÇÃO CONCLUÍDA ---")
    return {
        "divisão_complexa": division_result,
        "logaritmo_complexo": log_result if 'log_result' in locals() else None,
        "fatorial": factorial_result,
        "entropia_quântica": entropy_result,
    }

# Execução dinâmica
resultado = dynamic_quantum_demo()

# Exibição dos resultados
print("\nResultados da Demonstração:")
for chave, valor in resultado.items():
    print(f"{chave}: {valor}")
