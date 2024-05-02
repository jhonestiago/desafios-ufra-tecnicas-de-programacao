quantidade_1, valor_1, quantidade_2, valor_2, quantidade_3, valor_3 = map(float, input('Insira a quantidade e o respectivo valor unitário dos três produtos (ex: 10 20.00): ').replace(',','').split())

formula_total = quantidade_1 * valor_1 + quantidade_2 * valor_2 + quantidade_3 * valor_3

print(f'Valor Total: R$ {formula_total:.2f}')
