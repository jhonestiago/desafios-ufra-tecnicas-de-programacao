salario_atual:float = float(input('Insira o salário atual do funcionário: '))
taxa_reajuste:int = 25 # %

valor_reajuste = (salario_atual * taxa_reajuste) / 100
salario_reajustado = salario_atual + valor_reajuste

print(f'O novo salário é: R$ {salario_reajustado:.2f}')
