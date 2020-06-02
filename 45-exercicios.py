# O programa deve jogar jokenpô


import random

print("Agora vamos jogar")

escolha_usuario = int(input(
    "escolha uma das três opções:\n( 1 ) - Pedra\n( 2 ) - Papel\n( 3 ) - Tesoura "))

escolhas = [1, 2, 3]
escolha_pc = random.choice(escolhas)

if escolha_usuario == 1 and escolha_pc == 3:
    print(f"O usuario venceu!")
    if escolha_usuario == 2 and escolha_pc == 1:
        print(f"O usuario venceu!")
    if escolha_usuario == 3 and escolha_pc == 2:
        print(f"O usuario venceu!")
# elif escolha_usuario != 1 or escolha_usuario != 2 or escolha_usuario != 3:
#     print("Você escolheu uma opção invalida, tente novamente")
else:
    print("A maquina venceu!")
