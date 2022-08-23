from random import randint

print('''
\033[1:35m-=-=-=-=-=-=-=-=-=-\033[1:36m
      Jokenpô
\033[1:35m-=-=-=-=-=-=-=-=-=-\033[1:30m

Escolha sua opção:

[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura\033[m''')

escolha_usuario = int(input(''))
escolha_computador = randint(1, 3)

opcoes = {1 : "Pedra",
          2 : "Papel",
          3 : "Tesoura"}

try:
    if escolha_usuario == escolha_computador:
        print(f'\033[1:32mPC: {opcoes[escolha_computador]}\n\033[1:32mYOU: {opcoes[escolha_usuario]}\n\033[1:33mEMPATE!🤪')
    elif escolha_usuario == 1:
        if escolha_computador == 2:
            print(f'\033[1:32mPC: {opcoes[escolha_computador]}\n\033[1:32mYOU: {opcoes[escolha_usuario]}\n\033[1:33mPC GANHOU!😪')
        else:
            print(f'\033[1:32mPC: {opcoes[escolha_computador]}\n\033[1:32mYOU: {opcoes[escolha_usuario]}\n\033[1:33mYOU WIN!😉')
    elif escolha_usuario == 2:
        if escolha_computador == 1:
            print(f'\033[1:32mPC: {opcoes[escolha_computador]}\n\033[1:32mYOU: {opcoes[escolha_usuario]}\n\033[1:33mYOU WIN!😉')
        else:
            print(f'\033[1:32mPC: {opcoes[escolha_computador]}\n\033[1:32mYOU: {opcoes[escolha_usuario]}\n\033[1:33mPC GANHOU!😪')
    elif escolha_usuario == 3:
        if escolha_computador == 1:
            print(f'\033[1:32mPC: {opcoes[escolha_computador]}\n\033[1:32mYOU: {opcoes[escolha_usuario]}\n\033[1:33mPC GANHOU!😪')
        else:
            print(f'\033[1:32mPC: {opcoes[escolha_computador]}\n\033[1:32mYOU: {opcoes[escolha_usuario]}\n\033[1:33mYOU WIN!😉')
except:
    print('\033[1:31mERROR_OPÇÃO_INVÁLIDA!')
