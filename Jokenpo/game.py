import random

print('''Escolha uma opção:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')
opcao = int(input('Sua escolha:'))

[Pedra] = [1]
[Papel] = [2]
[Tesoura] = [3]

escolha = random.choice([1, 2, 3])

print('Minha escolha: {}'.format(escolha))

if escolha == 1 and opcao == 2:
    print('Papel embrulha a pedra, você ganhou!')
elif escolha == 2 and opcao == 1:
    print('Papel embrulha a pedra, você perdeu!')
elif escolha == 2 and opcao == 3:
    print('Tesoura corta o papel, você venceu!')
elif escolha == 3 and opcao == 2:
    print('Tesoura corta o papel, você perdeu!')
elif escolha == 1 and opcao == 3:
    print('Pedra quebra a tesoura, você perdeu!')
elif escolha == 3 and opcao == 1:
    print('Pedra quebra a tesoura, você venceu!')
else:
    print('Nós escolhemos a mesma opção, empatamos!')