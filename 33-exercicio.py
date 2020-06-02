# O programa deve ler 3 numeros e informar na tela qual é o maior e o menor entre eles


n1 = float(input("Informe o primeiro numero: "))
n2 = float(input("Informe o segundo numero: "))
n3 = float(input("Informe o terceiro numero: "))


if n1 > n2 and n1 > n3:
    print("O primeiro numero é o maior!")
elif n1 < n2 and n1 < n3:
    print("O primeiro numero é o menor!")
if n2 > n1 and n2 > n3:
    print("O segundo numero é o maior!")
elif n2 < n1 and n2 < n3:
    print("O segundo numero é o menor!")
if n3 > n1 and n3 > n2:
    print("O terceiro numero é o maior!")
elif n3 < n1 and n3 < n2:
    print("O terceiro numero é o menor!")
