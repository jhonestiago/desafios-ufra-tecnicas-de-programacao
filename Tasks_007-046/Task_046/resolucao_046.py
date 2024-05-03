diagonal_maior:float = float(input('Insira a medida da diagonal maior do losango (em cm): '))
diagonal_menor:float = float(input('Insira a medida da diagonal menor do losango (em cm): '))

area_losango = (diagonal_maior * diagonal_menor) / 2

print(f'A área do losango é: {area_losango:.2f} cm^2')
