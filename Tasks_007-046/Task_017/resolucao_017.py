nome_1, nome_2, nome_3 = map(str, input('Insira três nomes:\n').replace(',','').replace('e','').split())

print(f'{nome_3}, {nome_2} e {nome_1}')
