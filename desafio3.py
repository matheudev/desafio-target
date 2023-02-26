import json

# Carrega os dados do faturamento mensal de um arquivo JSON
with open('faturamento.json', 'r') as file:
    faturamentoMensal = json.load(file)

# Obtém o menor e o maior valor de faturamento ocorrido em um dia do mês
menorValor = min(faturamentoMensal)
maiorValor = max(faturamentoMensal)

# Calcula a média mensal de faturamento, ignorando dias sem faturamento
diasComFaturamento = [valor for valor in faturamentoMensal if valor != 0]
mediaMensal = sum(diasComFaturamento) / len(diasComFaturamento)

# Obtém o número de dias no mês em que o valor de faturamento diário foi superior à média mensal
diasAcimaDaMedia = sum(1 for valor in diasComFaturamento if valor > mediaMensal)

# Imprime os resultados
print(f"Menor valor de faturamento: R$ {menorValor:.2f}")
print(f"Maior valor de faturamento: R$ {maiorValor:.2f}")
print(f"Número de dias acima da média: {diasAcimaDaMedia}")
