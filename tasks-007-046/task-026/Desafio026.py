deposito:float = float(input('Insira o valor do deposito: ').replace(',','.'))
taxa_juros:float = float(input('Insira o valor da taxa de juros (%): ').replace(',','.').replace('%',''))

rendimento:float = deposito * (taxa_juros / 100)
valor_total:float = deposito + rendimento

print(f"Rendimento: R$ {rendimento:.2f}")
print(f"Valor Total: R$ {valor_total:.2f}")
