# O programa deve ler 7 o ano de nascimento de 7 pessoas e no final dizer quantas não sao maiores e quanta são maiores de idade.
from datetime import date


s = 0
total_maior = 0
total_menor = 0

for c in range(1, 8):
    ano_atual = date.today().year
    ano_nasc = int(input("Digite seu ano de nascimento: "))
    maioridade = ano_atual - ano_nasc
    if maioridade >= 21:
        total_maior += 1
    else:
        total_menor += 1
print(f"As pessoas que sao maiores de idade são {total_maior}")
print(f"As pessoas que sao maiores de idade são {total_menor}")
