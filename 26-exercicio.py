# O programa deve ler um nome ou fraze e dizer quantas vezes aparece a letra "a", qual foi a primeira vez e qual foi a ultima

nome = str(input("Digite seu nome ou texto: ")).strip().lower()


print(f"A letra A aparece {nome.count('a')} vezes")
print(f"A primeira posição em que ela aparece {nome.find('a')+1}")
print(f"A primeira posição em que ela aparece {nome.rfind('a')+1}")
