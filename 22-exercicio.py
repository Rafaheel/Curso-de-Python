# programa deve ler o nome completo de uma pessoa
# O nome com todas as letras maiusculas
# o nome com todas as letras minusculas
# quantas letras tem sem consicderar os espaços
# quantas letras tem o primeiro nome


nome = str(input("Digite seu nome completoto: ")).strip()


print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(" "))
print(nome.find(" "))
