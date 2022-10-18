from random import randint
from time import sleep

numero_pc = randint(1,10)

print("Um número foi escolhido!")
sleep(1)
print("Consegue advinhar qual número foi?")
sleep(1)

acertou = True 

tentativas = 0 

while acertou:
    palpite = int(input('Qual seu palpite?\n'))
    tentativas += 1
    if(palpite == numero_pc):
        acertou = False 
    else: 
        if (palpite < numero_pc): 
            print("Pensou errado! Meu número é maior!")
        elif (palpite > numero_pc): 
            print("Pensou errado! Meu número é menor!")

print("BOA! Acertou com " + str(tentativas) + " tentativas!")