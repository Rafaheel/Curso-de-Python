# O programa deve ler um numero inteiro e perguntar qual a conversao que o usuario deseja

from time import sleep


print(f"Bem vindo ao nosso conversor de moedas a seguir informe o valor que deseja converter!")
sleep(2)


valor = float(input("Informe o valor em R$: "))

opcao = int(input(
    "Escolha a moeda que deseja converter: \n ( 1 ) - Dólar Americano\n ( 2 ) - Euro "))


sleep(2)

if opcao == 1:
    dolar = 5.34
    dolar_real = valor / dolar
    print(
        f"Você informou que gostaria de converter R${valor}, com a cotação atual do Dólar de $ {dolar} você tera {dolar_real}")

elif opcao == 2:
    euro = 5.93
    euro_real = valor / euro
    print(
        f"Você informou que gostaria de converter R${valor}, com a cotação atual do Euro de $ {euro} você tera {euro_real}")
else:
    print("Você escolheu uma opção invalida, tente novamento mais tarde")
