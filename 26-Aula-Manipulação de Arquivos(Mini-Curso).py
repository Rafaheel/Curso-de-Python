'''
Usando a biblioteca write
'r' => usado para ler algo no arquivo
'w' => Usado para escrever algo
'r+' => usado para ler e escrever algo
'a' => usado para acrescentar algo
'''


valores_celurares = [850, 2230, 1500, 3500, 5000]

# with open("valores_celulares.txt", 'w') as arquivo:
#     for valor in valores_celurares:
#         arquivo.write(str(valor) + "\n")


# with open("valores_celulares.txt", 'a') as arquivo:
#     for valor in valores_celurares:
#         arquivo.write(str(valor) + "\n")


# with open("valores_celulares.txt", 'r') as arquivo:
#     for valor in valores_celurares:
#         print(valor)


# with open("valores_celulares.txt", 'a') as arquivo:
#     for valor in valores_celurares:
#         arquivo.write(str(valor) + "\n")

with open("valores_celulares.txt", 'r+') as arquivo:
    for valor in arquivo:
        print(valor)
    arquivo.write("9000")

