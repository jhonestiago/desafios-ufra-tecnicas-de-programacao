largura:float = float(input('Insira a largura do lote (em m): '))
comprimento:float = float(input('Insira o comprimento do lote (em m): '))

area_lote:float = largura * comprimento

print('Medidas do Lote')
print(f'Largura: {largura:.2f} m')
print(f'Comprimento: {comprimento:.2f} m')
print(f'Área: {area_lote:.2f} m^2')
