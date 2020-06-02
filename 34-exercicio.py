# O programa deve ler o salario de um fncionario e calcule o valor do seu aumento. para salario superiores a R$ 1.250,00, calcule aumento de 10%. Para superiores ou iguais, o aumento é de 15%.
from time import sleep


salario = float(input("Informe o valor a ser analisado: "))

if salario <= 1250:
    print("Estamos calculando...")
    sleep(2)
    sal_baixo = salario * 15/100
    print(
        f"O aumento possivel de acordo com a faixa salarial atual é de {salario + sal_baixo}")
else:
    print("Estamos calculando...")
    sleep(2)
    sal_alto = salario * 10/100
    print(
        f"O aumento possivel de acordo com a faixa salarial atual é de {salario + sal_alto}")
