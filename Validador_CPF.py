import re, sys

entrada = input("Digite o CPF a ser validado: ").strip()

CPF = re.sub(r'[^0-9]','',entrada)

if CPF[0] * len(CPF) == CPF:
    sys.exit()

soma_1dig = 0
fator = 10

# Os dígitos que serão calculados são retirados da iteração
for numero in CPF[:9]: 
    soma_1dig += (int(numero) * fator)
    fator -= 1

dig1 = (soma_1dig * 10) % 11 

dig1 = dig1 if dig1 < 10 else 0     # Adequação ao requisito do dígito do CPF

soma_2dig = 0
fator = 11

# Os dígitos que serão calculados são retirados da iteração
for numero in CPF[:10]: 
    soma_2dig += (int(numero) * fator)
    fator -= 1

dig2 = (soma_2dig * 10) % 11 

dig2 = dig2 if dig2 < 10 else 0     # Adequação ao requisito do dígito do CPF

final_calculado = str(dig1) + str(dig2)

if final_calculado == CPF[-2:]:
    print("CPF Válido!")
else:
    print("CPF Inválido!")