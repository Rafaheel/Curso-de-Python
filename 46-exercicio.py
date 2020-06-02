# O programa deve fazer uma contagem regressiva de 10 até zero.

from time import sleep

s = 0

for c in range(10, 0, -1):
    #s += 1
    sleep(1)
    print(f"{c}")
print(f"Viva!")
