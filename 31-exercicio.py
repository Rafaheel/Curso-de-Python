# O programa deve perguntar a distancia de uma viagem em Km. Calcule o preço da passagem, cobrando R$ 0,50 reais po km para viagens até 200 KM e R$ 0,45 para viagens mais longas.

from time import sleep


longa = 0.45
curta = 0.50

viagem = float(input("Informe a distancia da sua viagem: "))

if viagem <= 200:
    print(f"Calculando o preço da sua passagem, aguarde...")
    sleep(2)
    print(
        f"De acordo com a distancia informada de {viagem}Km\no valor a ser pago será de R$ {viagem * curta}")
else:
    print(f"Calculando o preço da sua passagem, aguarde...")
    sleep(2)
    print(
        f"De acordo com a distancia informada de {viagem}Km\no valor a ser pago será de R$ {viagem * longa}")
