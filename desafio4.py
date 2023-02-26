# Dicionário com os valores de faturamento de cada estado
faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Calcula o faturamento total mensal
total = sum(faturamento.values())

# Itera sobre o dicionário de faturamento para calcular o percentual de cada estado
for estado, valor in faturamento.items():
    percentual = (valor / total) * 100
    print(f'{estado}: {percentual:.2f}%')
