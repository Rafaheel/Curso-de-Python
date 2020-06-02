# Faça um algoritimo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.


preco = float(input("Informe o o preço para calcularmos o desconto: "))
desconto = 5/100
novo_preco = preco * desconto
print(
    f"O preço do produto é de {preco}, já o desconto disponivel para ele é de {desconto}, sendo assim o novo preço é {preco - novo_preco}")
