# o programa deve ler a velocidade de um carro, se ele ultrapassar 80KM/h mostrar mensagem de multa. Também mostrar o valor que vai custar o a multa pelo excesso de velocidade, custa 7km/h por cada km/h acima do limite
import time

limite = 80
valor_multa = 7


velo = int(input("Qual a velocidade a ser analisada: "))

if velo <= limite:
    time.sleep(2)
    print(
        f"Parabéns, você passou a {velo}KM/h, e esta dentro do limite permitido")
else:
    time.sleep(2)
    multa = (limite - velo) * -1
    print(
        f"Estamos analisando, sua velocidade foi de {velo}KM/h, \n desta forma você excedeu em {multa}KM/h")
    time.sleep(2)
    print("Estamos calculando o valor da sua multa")
    time.sleep(2)
    print(f"O valor total de sua multa foi de R${valor_multa * multa}")
