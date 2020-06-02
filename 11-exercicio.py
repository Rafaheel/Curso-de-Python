# Faça um programa que leia a largura, a altura de uma parede em metros calcule sua area e aquantidade de tinta necessaria para pinta-lá, saabendo que cada litro de tinta pinta uma area de 2metros quadrados.

largua = float(input("Informe a largura: "))
altura = float(input("Informe a altura: "))
area = largua * altura
lata_tinta = 2

print(f"A largura é {largua}, a altura é {altura}, então sua area é de {area}m, \nassim sendo será necessario {area / lata_tinta} litros de tinta")
