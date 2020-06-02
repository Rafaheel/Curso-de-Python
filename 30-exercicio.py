# programa deve ler se um numero é par ou ímpar


n = int(input("Digite um numero: "))

resultado = n % 2


if resultado == 0:
    print(f"O numero escolhido é par")
else:
    print(f"O numero escolhido é impar")
