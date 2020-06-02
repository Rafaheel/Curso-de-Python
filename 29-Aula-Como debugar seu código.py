import random

# class EmailDeBoasVindas:
#     def __init__(self):
#         self.pessoas = ['Cristian', 'Robert', 'Rossana', 'Ana']

#     def Iniciar(self):
#         emails_apresentacao = self.MontarCredencial(self.pessoas)
#         for email in emails_apresentacao:
#             print(email)
#             print(emails_apresentacao[5])

#     def MontarCredencial(self, pessoas):
#         credenciais = []
#         for pessoa in pessoas:
#             credenciais.append(
#                 f'A empresa gostaria de dar as boas vindas para o(a) {pessoa}')
#         return credenciais


# email = EmailDeBoasVindas()
# email.Iniciar()


# F5 começa a debugar o codigo
# F10 analisa linha por linha
# F11 Analisa a linha e entra no codigo interno
# Shif + F11 sai do bloco do codigo atual e continua a execução


# Desafio


class EmailDeBoasVindas:
    def __init__(self):
        self.pessoas = ['Cristian', 'Robert', 'Rossana', 'Ana']

    def Iniciar(self):
        # inicie o debug aqui (coloque um breakpoint)
        print('Olá bem vindo a este site!')
        self.ChutarIdade(self.pessoas)  # Pule essa linha
        self.ChutarNome()  # Entre dentro do método dessa linha
        self.ChutarCor()  # Entre neste método
        # Para a execução aqui novamente usando um break point
        print('Programa finalizado')

    def ChutarCor(self):
        cores = ['azul', 'rosa', 'verde', ]
        for cor in cores:
            print(f'as opções de cores são: {cor}')

        # não continue a execução aqui, volte para onde estava antes
        print('sua cor favorita é...')
        cor_preferida = random.choice(cores)
        print(cor_preferida)

    def ChutarNome(self):
        nome = f'bem vindo {random.choice(self.pessoas)}'
        print(nome)

    def ChutarIdade(self, pessoas):
        # Entre aqui
        idade = random.randint(18, 50)
        print(idade)


email = EmailDeBoasVindas()
email.Iniciar()
