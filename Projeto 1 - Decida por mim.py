import random
import time


class DecidaPorMim:
    def __init__(self):
        self.respostas = ["Não faço ideia",
                          "Você tem certesa disso?", "o que você acha disso?",
                          "Obvio", "Sem chance", "Sim, com certeza", "Eu realmente não sei", "Já vi isso antes",
                          "Definitivamente não!", "Talvez você deveria esperar mais um pouco"
                          ]

    def Iniciar(self):
        self.FazerPergunta()

    def FazerPergunta(self):
        input("Qual sua duvida?: ")
        print("Pensando...")
        time.sleep(2)
        print(random.choice(self.respostas))
        fazer_outra_pergunta = input(
            "Gostaria de fazer uma nova pergunta? (s/n): ")
        if fazer_outra_pergunta == "s":
            self.FazerPergunta()
        elif fazer_outra_pergunta == "n":
            print("obrigado por usar nosso programa!")
        else:
            print("Favor digitar apenas 's' ou 'n'")
            self.FazerPergunta()


decida_por_mim = DecidaPorMim()
decida_por_mim.Iniciar()
