# O programa deve ler seis numeros inteiros e mostrar apenas a soma dos numeros pares


s = 0
cont = 0

for c in range(1, 6 + 1):
    n = int(input("Digite um numero: "))
    if n % 2 == 0:
        s += n
        cont += 1
print(f"Você escolheu {cont} pares e o somatorio é {s}")
