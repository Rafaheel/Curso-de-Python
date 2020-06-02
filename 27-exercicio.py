# o programa deve ler o nome e mostrar o nome e sobre nome


nome = str(input("Digite seu nome completo: ")).strip().lower()
nome_dividido = nome.split()


print(f"Primeiro nome: {nome_dividido[0]}")
print(f"Primeiro nome: {nome_dividido[len(nome_dividido)-1]}")
