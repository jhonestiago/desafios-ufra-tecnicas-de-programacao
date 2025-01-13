massa_kg:float = float(input('Insira o seu peso (em kg): '))

# 1) Massa em gramas
massa_g = massa_kg * 1000

# 2) Ganho de massa (5%)
ganho_massa = (massa_g * 5) / 100
nova_massa_g = massa_g + ganho_massa

# SAIDA
print(f'Peso em gramas: {massa_g:.2f} g')
print(f'Novo peso: {nova_massa_g:.2f} g')
