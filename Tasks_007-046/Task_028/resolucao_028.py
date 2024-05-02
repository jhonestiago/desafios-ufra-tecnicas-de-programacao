salario_funcionario:float = float(input('Insira o valor do salário do funcionário: '))
salario_minimo:float = float(input('Insira o valor do salário mínimo: '))

total_salarios = salario_funcionario / salario_minimo

print(f'O funcionario ganha {total_salarios:.2f} salários mínimos')
