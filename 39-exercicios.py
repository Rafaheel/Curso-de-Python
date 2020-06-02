# o programa deve ler o ano de um jovem e dizer se ele ainda vai, é hora, ou já passou da hora de se alistar.
from datetime import date

ano_nasc = int(input(
    "Bom jovem chegou a hora de verificar se você ira carpir meio fio\ninforme seu ano de nascimento: "))


ano_atual = date.today().year
ano_alistamento = ano_atual - ano_nasc

if ano_alistamento < 18:
    print("Ainda não chegou sua hora jovem!")
    print(f"Ainda faltam {18 - ano_alistamento} anos")
elif ano_alistamento == 18:
    print("Chegou a sua hora de carpir jovem!")
    print(ano_alistamento)
else:
    print("Já passou da hora vovo!")
    print(f"Você sa se alistou a {ano_alistamento - 18} anos")
