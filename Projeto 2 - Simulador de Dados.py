import random
import time

print(random.randint(1, 6))
resposta = input("Deseja tentar outro numero? (s/n) ")


if resposta == 's':
    print(random.randint(1, 6))
    resposta = input("Deseja tentar outro numero? (s/n) ")
elif resposta == 'n':
    print("Obrigado por jogar")
else:
    print("digite apenas s ou n ")
    resposta = input("Deseja tentar outro numero? (s/n) ")

