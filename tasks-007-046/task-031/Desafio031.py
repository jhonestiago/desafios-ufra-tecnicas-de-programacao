salario:float = float(input('Insira o valor do salário do funcionário: '))
taxa_IR:int = 5 # Taxa do Imposto de Renda (%)

valor_IR = (salario * taxa_IR) / 100

print(f'Valor do imposto de renda a ser pago: R$ {valor_IR:.2f}')
