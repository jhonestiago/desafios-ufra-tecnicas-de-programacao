salario_minimo:float = float(input('Insira o valor do salário mínimo: '))
kW_consumidos:float = float(input('Insira a quantidade de kW consumidos: '))

# 1) Valor em reais (cada kWh)
valor_kWh = (salario_minimo * 2) / 100

# 2) Valor Total a ser pago pela residência
valor_total = valor_kWh * kW_consumidos

# 3) Valor com desconto de 15 %
desconto = (valor_total * 15) / 100
valor_reajustado = valor_total - desconto

print(f'Valor do quilowatt: R$ {valor_kWh:.2f}')
print(f'Valor Total: R$ {valor_total:.2f}')
print(f'Valor com desconto de 15%: R$ {valor_reajustado:.2f}')
