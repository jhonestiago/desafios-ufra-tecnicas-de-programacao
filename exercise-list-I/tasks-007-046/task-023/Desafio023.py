valor_1, valor_2, valor_3, valor_4 =  map(float, input('Insira quatro valores: ').replace(',','.').split())

somatorio = valor_1 + valor_2 + valor_3 + valor_4
media = somatorio / 4

perc_valor_1 = (valor_1 / somatorio) * 100
perc_valor_2 = (valor_2 / somatorio) * 100
perc_valor_3 = (valor_3 / somatorio) * 100
perc_valor_4 = (valor_4 / somatorio) * 100

print(f'Média = {media}')
print(f'Σ = {somatorio}')
print(f'{valor_1} corresponde a {perc_valor_1:.2f}% de {somatorio}')
print(f'{valor_2} corresponde a {perc_valor_2:.2f}% de {somatorio}')
print(f'{valor_3} corresponde a {perc_valor_3:.2f}% de {somatorio}')
print(f'{valor_4} corresponde a {perc_valor_4:.2f}% de {somatorio}')
