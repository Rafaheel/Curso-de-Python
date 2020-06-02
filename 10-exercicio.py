# crie um programa que leia quanto dinheiro  uma pessoa tem na carteira e mostra quantos dolares el pode comprar

cotacao = 3.27
valor = float(input("Informe quantos reais deseja converter: "))
print("Cotação do dolar atual é R$ 3,27")

print(
    f"A quantia solicitada foi de {valor}, sendo assim em conversão direta é possivel é: {valor / cotacao} ")
