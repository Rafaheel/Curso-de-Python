# Uma batalha de um RPG.
import random
import time


print('\033[1;30mEm uma terra muito distante um guerreiro surge...\033[m')
time.sleep(3)
personagem = input('\033[1;30mEscolha o nome do seu guerreiro:\033[m').capitalize()


adv1 = 'Ogro'
adv2 = 'Mago Negro'
adv3 = 'Ciclope'
lista = [adv1, adv2, adv3]


inimigo = random.choice(lista)
time.sleep(2)
print('Agora \033[36m{}\033[m, você enfrentará seu primeiro desafio! Prepare - se!'.format(personagem, inimigo))

personagemvida = 20
inimigovida = 20
ataqueper = (10 * random.random())
ataqueini = (10 * random.random())


jogada = str(input('\033[1;30mDeseja atacar? sim/não:\033[m '))
time.sleep(2)


while jogada != 'sim':
    time.sleep(2)
    print('\033[7;31;40mVocê precisa escolher a opção sim para iniciar sua jornada!\033[m')
    time.sleep(2)
    jogada = str(input('\033[1;30mDeseja atacar? sim/não:\033[m '))

print('\033[1;30mAndando por uma floresta escura {} encontra seu primeiro inimigo, o assustador\033[m...\033[31m{}\033[m'.format(personagem, inimigo))


while personagemvida and inimigovida > 0:
    ataqueper = (10 * random.random())
    ataqueini = (10 * random.random())

    while jogada != 'sim':
        time.sleep(2)
        print('\033[7;31;40mVocê precisa escolher a opção sim para iniciar sua jornada!\033[m')
        time.sleep(2)
        jogada = str(input('Deseja atacar? sim/não: '))

    if jogada == 'sim':
        time.sleep(1)
        print('Você esta atacando {} com uma espada...'.format(inimigo))
        time.sleep(2)
        print('Seu golpe gerou um dano de {:.0f} no {}'.format(ataqueper, inimigo))

        inimigovida = inimigovida - ataqueper

        if inimigovida <= 0:
            print('\033[1;30mParabéns {}, ao fim de uma ardua batalha, você venceu o jogo!\033[m'.format(personagem))
        if inimigovida > 0:
            time.sleep(2)
            print('Prepare - se para o ataque do {}'.format(inimigo))
            time.sleep(2)
            print('O {} atacou, você recebeu um dano de {:.0f}'.format(inimigo, ataqueini))
            personagemvida = personagemvida - ataqueini

        if personagemvida <= 0:
            time.sleep(2)
            print('{}\033[1;30mvocê recebeu muitos golpes e foi derrotado por um {}\033[m'.format(personagem, inimigo))

