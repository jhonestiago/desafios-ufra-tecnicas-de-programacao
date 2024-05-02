cotacao_dolar:float = float(input('Insira a cotação do dolar no dia: ').replace(',','.'))
quantia_dolares:float = float(input('Insira a quantia em dolares: ').replace(',','.'))

quantia_reais = quantia_dolares * cotacao_dolar

print(f'US$ {quantia_dolares} = R$ {quantia_reais}')
