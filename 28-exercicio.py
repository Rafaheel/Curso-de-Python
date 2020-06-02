# o programa deve pensar em um numero de 0 a 5 e peça para o usuario tentar descobrir o numero escolhido pelo computador. o programa deve dizer quem venceu ou perdeu


import random
import time

numero_pc = random.randint(0, 5)
time.sleep(2)
print(f"Eu penseim em um numero de 0 a 5, tente adivinhar...")
time.sleep(2)
resposta = int(input("Qaul numero você acha que é: "))

if numero_pc == resposta:
    time.sleep(2)
    print(f"exatamente eu pensei {numero_pc}")
else:
    time.sleep(2)
    print(
        f"Não foi dessa vez eu pensei em {numero_pc} e você disse {resposta} \n Tente novamente mais tarde.")
