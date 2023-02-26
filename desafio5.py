# Pede ao usuário para digitar um texto
texto = input("Digite um texto: ")

# Inicializa a variável que irá armazenar o texto invertido
texto_invertido = ""

# Percorre o texto de trás para frente e adiciona cada caractere na variável texto_invertido
for i in range(len(texto)-1, -1, -1):
    texto_invertido += texto[i]

# Imprime o texto invertido
print(f"O texto invertido é: {texto_invertido}")