import random
from time import sleep

n_rounds = 5

gestures = ['pedra', 'papel', 'tesoura', 'serpente', 'spock']

dict_perde = {'pedra': ['papel', 'spock'], 'tesoura':['pedra','spock'], 'papel':['tesoura', 'serpente'], 'serpente':['pedra', 'tesoura'], 'spock':['papel', 'serpente']}

rounds_to_win = n_rounds - 1

rounds = 0

cpu_score = 0

player_score = 0

def escolha_do_jogador():
    print('Escolha: pedra, papel, tesoura, serpente, spock')
    x=input()
    for item in x:
        if x == 'pedra' or x == 'tesoura' or x == 'papel' or x == 'serpente' or x == 'spock':
            return x
        else:
            x = input()
            


while rounds < 2:
    rounds += 1
    y = random.choice(list(dict_perde.keys()))
    x = escolha_do_jogador()
    
    if x not in dict_perde.keys():
        print('Escolha uma opção válida!')
    else:
        print('Escolha do Computador: ' +y)
        if y in dict_perde[x]:
            print('voce perdeu')
            cpu_score += 1
        elif x==y:
            print('empate')
        else:
            print('voce ganhou')
            player_score += 1
            
        print('Pontuação do computador: ' +str(cpu_score)+' Pontuação do Jogador: '+str(player_score))
        print('Round: ' +str(rounds) + '\n')
    
if cpu_score > player_score:
    print('Computador Ganhou!')
    
elif cpu_score < player_score:
    print('Jogador Ganhou!')
    
else:
    print('Você e o Computador Ficaram Empatados!')