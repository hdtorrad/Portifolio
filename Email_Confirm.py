#Desafio criar um sistema para mostrar apenas uma parte do e-mail

email= input("Digite o email: ")

nome_email = email[:email.find('@')]
dominio = email[email.find('@'):]

INDICE = round(len(nome_email) * 0.2) #emails muito grandes precisam exibir mais letras

# A expressão que contém a função len() permite que o e-mail fique com seu tamanho original
email_seguro = f'{nome_email[:INDICE]}' + (len(nome_email) - (INDICE * 2)) * '*' + f'{nome_email[-INDICE:]}' + dominio

print(f'Exibição segura do e-mail para confirmação: \n{email_seguro}')