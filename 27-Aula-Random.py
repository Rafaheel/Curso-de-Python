# exemplo cara ou coroa

import random


print(random.random())  # Valor 0.0 atá 1.0
print(random.uniform(4, 10))  # Valor decimal minimo e maximo
print(random.randint(12, 55))  # Valor inteira do minimo e maximo


cores = ["verde", "vermelho", "azul"]
# Escolhe aleatoriamento o elemento dentro da lista
print(random.choice(cores))


cartas_baralho = ["carta1", "carta2", "carta3", "carta4", "carta5"]
random.shuffle(cartas_baralho)
print(cartas_baralho)


# Desafio 1 Cara ou Coroa
moeda = ["cara", "coroa"]
print(random.choice(moeda))


# Desafio 2 Sorteio de nomes

nomes = ["Rafael", "Julia", "Jemmefer", "China"]
print(random.choice(nomes))

print(random.randint(10, 100))
