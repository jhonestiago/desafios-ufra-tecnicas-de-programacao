base:float = float(input('Insira o tamanho da base do triângulo (em cm): '))
altura:float = float(input('Insira o tamanho da altura do triângulo (em cm): '))

area_triangulo:float = (base * altura) / 2

print(f'A área do triângulo é: {area_triangulo:.2f} cm^2')
