ano_nascimento:int = int(input('Insira o ano de nascimento (0000): '))
ano_atual:int = int(input('Insira o ano atual (0000): '))

idade_anos:int = ano_atual - ano_nascimento
idade_semanas:int = idade_anos * (365 // 7)

print(f'Idade: ~ {idade_anos} anos')
print(f'Idade em semanas ~ {idade_semanas} semanas')
