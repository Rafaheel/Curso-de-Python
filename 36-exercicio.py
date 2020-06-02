# Programa deve aprovar um emprestimo bancario para uma compra de uma casa. O programa vai perguntar o valor da casa o salario do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ele nao pode exceder 30% do salario ou então o emprestimo será negado.

from time import sleep


nome = str(
    input(f"Por favor se informe seu nome para que possamos identifica-lo(a): ")).strip().capitalize()
sleep(2)

print(f"Aguarde {nome}, estamos procurando seu cadastro!")
sleep(2)

salario = float(input(
    f"Olá {nome}, bem vindo(a) ao nosso simulador de credito imobiliario, para iniciar informe seus rendimentos mensais: "))

print(f"Aguarde {nome}, estamos processando!")
sleep(2)

valor_imovel = float(input(f"Informe também, o valor do imovel: "))
sleep(2)

prazo = int(input(f"Informe o prazo do seu financiamento (em anos): "))

ini_financ = str(
    input("Deseja iniciar sua similação agora? (s/n): ")).strip().lower()
sleep(2)


if ini_financ == "n":
    sleep(2)
    print(f"Que pena {nome}, esperamos que volte logo!")

elif ini_financ == "s":
    print(f"Ok {nome}, estamos processando")
    sleep(2)
    prazo_ajustado = prazo * 12
    comprometimento_maximo = salario * 30/100
    parcela = valor_imovel / prazo_ajustado
    if parcela > comprometimento_maximo:
        sleep(2)
        print(
            f"Infelizmente {nome}, nas condiçoes propostas, seu emprestimo não foi aprovado, sugerimos se dirigir a sua agência.")
    else:
        print(f"Bom {nome}, nas condições proposta o valor da sua parcela ficaria em torno de R$ {parcela},\ncom um prazo de {prazo} anos")
