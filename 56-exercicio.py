# o programa deve ler o  nome idade e sexo de 4 pessoas e no final mostrar a media da idade, o nome do homem mais velhoe quantas mulheres tem menos de 20 anos


maior_idade_homem = 0
nome_homem_velho = 0
total_mulher_20 = 0

s = 0
for c in range(1, 5):
    nome = str(input("Digite seu nome: ")).strip()
    sexo = str(input("Digite seu sexo (m/f): ")).strip().lower()
    idade = int(input("Digite sua idade: "))
    s += idade

    if c == 1 and sexo == "m":
        maior_idade_homem = idade
        nome_homem_velho = nome
    if sexo == "m" and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_homem_velho = nome
    if sexo == "f" and idade < 20:
        total_mulher_20 += 1


print(f"a média da idade é de {s / c}")
print(
    f" O nome do homem mais velho é {nome_homem_velho} e sua idade é de {maior_idade_homem} anosj")
print("Ao todo são {} mulheres com menos de 20 anos!")
