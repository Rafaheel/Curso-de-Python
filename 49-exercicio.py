# O programa deve mostrar a tabuado do numero que o usuario escolher usando laço for


n = int(input("Digite o numero: "))


for c in range(1, 11):
    print(f"{n} X {c}: {n * c} ")
print("Acabou")
