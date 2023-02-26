"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os
palavra_secreta = "Medo"
palavra_formatada = "****"
tentativas = 1

while True:
    
    letra_digitada = input("Insira uma letra: ")
    
    if len(letra_digitada) > 1:
        print("Insira apenas uma letra!")
        continue        
    
    if letra_digitada in palavra_secreta:

        for i in range(len(palavra_secreta)):

            if letra_digitada == palavra_secreta[i]:

                palavra_formatada = palavra_formatada[:i] + palavra_secreta[i] + palavra_formatada[(i+1):]
    
        print(f"Palavra até agora: \n{palavra_formatada}")
    
    else:
        print("Letra não encontrada!")        

    if len(palavra_formatada.replace('*', '')) == len(palavra_secreta):        
        os.system("cls")
        print(f"Você Ganhou!\nCom {tentativas} tentativas!")
        break

    else:
        tentativas += 1
