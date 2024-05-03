import math

a:float = float(input('Insira o valor de a: '))
b:float = float(input('Insira o valor de b: '))
c:float = float(input('Insira o valor de c: '))

delta = (b ** 2) - (4 * a * c)

raiz_1 = ((-b) + math.sqrt(delta)) / (2 * a)

raiz_2 = ((-b) - math.sqrt(delta)) / (2 * a)

print(f'Δ = {delta}')
print(f"x' = {raiz_1:.2f}")
print(f'x" = {raiz_2:.2f}')
