import logging


logging.basicConfig(
    filename="excp.log",
    level=logging.DEBUG,
    format="%(levelname)s %(asctime)s: %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
)

logger = logging.StreamHandler()
logging.getLogger("").addHandler(logger)


try:
    ano_atual = int(input("Qual é o ano atual?"))
except ValueError:
    logging.warning("Você deve digitar um numero.")


try:
    print(5/0)
except ZeroDivisionError:
    logging.warning("Não é possivel efetuar uma divião por 0.")


try:
    print(10/0)
except:
    logging.warning("Não é possivel efetuar uma divião por 0.")
finally:
    logging.info("Usuario X  realizou calculos no sistema.")

# for pagina in range(10):
#     try:
#         print("buscando sites")
#         print(5/0)
#     except:
#         pass
