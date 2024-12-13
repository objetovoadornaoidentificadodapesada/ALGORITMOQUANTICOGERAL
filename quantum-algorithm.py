import math
import cmath  # Para cálculos complexos

# Função principal para simular o protótipo
def quantum_algorithm_demo():
    print("===== MECÂNICA QUÂNTICA: PROTOTIPAGEM COMPUTACIONAL =====")
    
    # Definição de constantes quânticas e entradas
    h_bar = 1.0545718e-34  # Constante de Planck reduzida (em Joules-segundo)
    pi = math.pi
    quantum_input = complex(0.707, 0.707)  # Vetor normalizado na esfera quântica
    
    # 1. Demonstração de divisões complexas
    def complex_division(z1, z2):
        try:
            result = z1 / z2
            return result
        except ZeroDivisionError:
            return "Divisão por zero não permitida no domínio quântico"
    
    z1 = quantum_input
    z2 = complex(math.e, pi)
    division_result = complex_division(z1, z2)
    
    print(f"Divisão de números complexos: {z1} / {z2} = {division_result}")
    
    # 2. Cálculo de logaritmo complexo
    def quantum_logarithm(z):
        if z == 0:
            raise ValueError("Logaritmo indefinido para zero.")
        magnitude = abs(z)
        phase = cmath.phase(z)
        return complex(math.log(magnitude), phase)
    
    log_result = quantum_logarithm(quantum_input)
    print(f"Logaritmo complexo: log({quantum_input}) = {log_result}")
    
    # 3. Performance matemática no tempo
    def factorial_performance(n):
        """Cálculo do fatorial para simular carga computacional."""
        if n == 0 or n == 1:
            return 1
        return n * factorial_performance(n - 1)
    
    n = 10
    factorial_result = factorial_performance(n)
    print(f"Fatorial de {n}: {factorial_result}")
    
    # 4. Interpretação de entropia quântica
    def quantum_entropy(probabilities):
        """Calcula a entropia quântica de um conjunto de probabilidades."""
        entropy = 0
        for p in probabilities:
            if p > 0:
                entropy -= p * math.log2(p)
        return entropy
    
    # Probabilidades de um sistema de dois estados
    probabilities = [0.5, 0.5]  # Superposição igual
    entropy_result = quantum_entropy(probabilities)
    print(f"Entropia quântica: {entropy_result} bits")
    
    # Demonstração final
    print("\n--- DEMONSTRAÇÃO CONCLUÍDA ---")
    return {
        "divisão_complexa": division_result,
        "logaritmo_complexo": log_result,
        "fatorial": factorial_result,
        "entropia_quântica": entropy_result,
    }

# Chamada principal
resultado = quantum_algorithm_demo()

# Visualização detalhada do resultado
for chave, valor in resultado.items():
    print(f"{chave}: {valor}")
