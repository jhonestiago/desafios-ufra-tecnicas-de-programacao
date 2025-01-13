comprimento:float = float(input("Insira o comprimento da piscina (em m): ").replace(",","."))
largura:float = float(input("Insira a largura da piscina (em m): ").replace(",","."))
profundidade:float = float(input("Insira a profundidade da piscina (em m): ").replace(",","."))
valor_m3:float = 75.00

volume:float = comprimento * largura * profundidade
valor_total:float = volume * valor_m3

print(f"O valor total da piscina é R$ {valor_total:.2f}")
