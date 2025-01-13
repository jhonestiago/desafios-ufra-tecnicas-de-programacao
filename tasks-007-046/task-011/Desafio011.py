distancia:float = float(input('Insira a distância percorrida (em km): ').replace(",","."))
litros:float = float(input('Insira a quantidade de litros consumidos: ').replace(",","."))

taxa_consumo:float = distancia / litros

print(f'A taxa de consumo é: {taxa_consumo:.2f} km/l')
