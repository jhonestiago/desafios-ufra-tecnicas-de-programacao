# Algoritmo preco_automovel

nome_automovel:str = input('Insira o nome do automóvel: ')
preco_fabrica:float = float(input('Insira o preco de fábrica: '))

valor_impostos:float = preco_fabrica * 0.45
percentagem_revendedor:float = preco_fabrica * 0.28
preco_final:float = preco_fabrica + valor_impostos + percentagem_revendedor

print(f'Nome do automóvel: {nome_automovel}')
print(f'Preço final: R$ {preco_final:.2f}')
