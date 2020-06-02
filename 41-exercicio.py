# O programa deve ler a idade o ano de nascimento e classifique de acordo a faixa de idade
from datetime import date

ano_nasc = int(input("Por favor, informe o seu ano de nascimento: "))

ano_atual = date.today().year
idade = ano_atual - ano_nasc


if idade <= 9:
    print(f"Você tem {idade} anos, sua categoria é Mirim!")
elif idade > 9 and idade <= 14:
    print(f"Você tem {idade} anos, sua categoria é Infantil!")
elif idade > 14 and idade <= 19:
    print(f"Você tem {idade} ano, sua categoria é Junior")
elif idade > 19 and idade <= 25:
    print(f"Você tem {idade} ano, sua categoria é Sênior")
else:
    print(f"Você tem {idade} ano, sua categoria é Master!")
