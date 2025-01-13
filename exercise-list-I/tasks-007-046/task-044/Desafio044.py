base_maior:float = float(input('Insira a medida da base maior do trapézio (em cm): '))
base_menor:float = float(input('Insira a medida da base menor do trapézio (em cm): '))
altura:float = float(input('Insira a medida da altura do trapézio (em cm): '))

area_trapezio = ((base_maior + base_menor) * altura) / 2

print(f'A área do trapézio é: {area_trapezio:.2f} cm^2')
