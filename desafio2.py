# Pede o usuário para digitar um número para ser verificado
n = int(input("Digite um número: "))

# Define a função fibonacci que recebe um número n e checa se ele pertence à sequência Fibonacci ou não
def fibonacci(n):
    x = 0
    y = 1
    while (x < n):
        z = x
        x = y
        y += z
    if x == n:
        return f"O número {n} pertence à sequência de Fibonacci"
    else:
        return f"O número {n} não pertence à sequência de Fibonacci"

# Chama a função fibonacci com o número digitado e imprime o resultado
answer = fibonacci(n)
print(answer)