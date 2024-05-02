idade:int = int(input('Insira a idade da pessoa: '))

idade_meses = idade * 12
idade_dias = idade_meses * 365
idade_horas = idade_dias * 24
idade_minutos = idade_horas * 60

print(f'Idade em meses: {idade_meses} meses')
print(f'Idade em dias: {idade_dias} dias')
print(f'Idade em horas: {idade_horas} horas')
print(f'Idade em minutos: {idade_minutos} minutos')
