# O programa deve ler o valor a ser pago pelo produto de acordo com a condição de pagamento


valor = float(input("Informe o valor do produto: "))


condicao = int(input(
    "Informe a condição de pagamenot:\n( 1 ) - Á Vista, com dinheiro ou cheque possui 10 de desconto)\n( 2 ) - O preço normal dividido em duas parcelas)\n( 3 ) - Três ou mais parcelas nocartão, possui acressimo de 20 de juros)"))


if condicao == 1:
    novo_valor = valor - (valor * 10/100)
    print(f"O valor total a pagar é de R$ {novo_valor}")
elif condicao == 2:
    print(
        f"O valor total a pagar é R$ {valor}, é possivel parcelar em até duas vezes no cartão")
elif condicao == 3:
    novo_valor = valor + (valor * 20/100)
    print(
        f"O valor total a pagar é de R$ {novo_valor}, lembrando que é possivel parcelar em até 3 vezes no cartão")
else:
    print("Você não escolheu uma condição valida, por favor tente novamente")
