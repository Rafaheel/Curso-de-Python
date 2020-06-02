# o programa deve ler o peso de 5 pessoas e mostrar qual foi o maio peso e o menor peso


maior = 0
menor = 0


for p in range(1, 6):
    peso = float(input("Informe seu peso: "))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f"O maior peso lido foi de {maior}Kg")
print(f"O menor peso lido foi de {menor}Kg")
