
# try:
#     ano_atual = int(input("Qual é o ano atual?"))
# except ValueError:
#     print("Você precisa digitar um numero!")


# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("Não é possivel efetuar a divisão por zero!")


# try:
#     print(10/0)
# except:
#     print("Ocorreu um erro!")
# finally:
#     print("O usuario X realizou calculos no sistema.")

for pagina in range(10):
    try:
        print("buscando sites")
        print(5/0)
    except:
        pass
