# O programa deve ler dois numeros inteiros e compara -los dizendo se são iguais e qual é o valor menor e maior


print("Vamos analisar dois numeros, a seguir informe-os")

n1 = int(input("Informe o primeiro numero: "))
n2 = int(input("Informe o segundo numero: "))

if n1 == n2:
    print(
        f"O primeiro numero foi {n1}, já o segundo foi {n2}, desta forma eles são iguais!")
elif n1 > n2:
    print(f"O primeiro numero é maior {n1}")
else:
    print(f"O segundo numero é maior {n2}")
