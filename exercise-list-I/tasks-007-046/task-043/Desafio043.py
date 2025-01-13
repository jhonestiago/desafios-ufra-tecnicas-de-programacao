import math

raio:float = float(input('Insira a medida do raio do círculo (em cm): '))

area_circulo = math.pi * (raio ** 2)

print(f'A área do círculo é: {area_circulo:.2f} cm^2')
