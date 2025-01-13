nota_1, peso_1 = map(float, input('Insira a nota do aluno na 1ª Avaliação e o respectivo peso: ').replace(',','.').split())
nota_2, peso_2 = map(float, input('Insira a nota do aluno na 2ª Avaliação e o respectivo peso: ').replace(',','.').split())

som_Np = (nota_1 * peso_1) + (nota_2 * peso_2)
som_pesos = peso_1 + peso_2
media_ponderada = som_Np / som_pesos

print(f'Média Ponderada = {media_ponderada:.2f}')
