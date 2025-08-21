import sys

print('---------- VALIDADOR DE CPF ----------')

# Recebe um CPF digitado pelo usuário.
cpf = input('Digite um CPF: ')
cpf_completo = ''

# Verifica se o texto digitado é um número e se o CPF tem 11 dígitos.
if cpf.isnumeric() and len(cpf) == 11:
    # Formata o CPF na estrutura XXX.XXX.XXX-XX
    cpf_completo = f"{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

    # Calcula o 10º dígito.
    peso_digito10 = 10
    soma_digito10 = 0
    digito10 = 0
    for n in cpf[0:9]:
        num = int(n)
        soma_digito10 += num * peso_digito10
        peso_digito10 -= 1

    resultado_digito10 = soma_digito10 % 11

    # Verifica o valor correto do 10º dígito.
    if resultado_digito10 == 0 or resultado_digito10 == 1:
        digito10 = 0
    else:
        digito10 = 11 - resultado_digito10

    # Verifica se o valor correto do 10º dígito é igual ao do CPF informado pelo usuário.
    if int(cpf[9]) != digito10:
        print('O 10º dígito do CPF informado é inválido!')
        sys.exit()  # Interrompe o programa

    # Calcula o 11º dígito.
    peso_digito11 = 11
    soma_digito11 = 0
    digito11 = 0
    for n in cpf[0:10]:
        num = int(n)
        soma_digito11 += num * peso_digito11
        peso_digito11 -= 1

    resultado_digito11 = soma_digito11 % 11

    # Verifica o valor correto do 11º dígito.
    if resultado_digito11 == 0 or resultado_digito11 == 1:
        digito11 = 0
    else:
        digito11 = 11 - resultado_digito11

    # Verifica se o valor correto do 11º dígito é igual ao do CPF informado pelo usuário.
    if int(cpf[10]) != digito11:
        print('O 11º dígito do CPF informado é inválido!')
        sys.exit()  # Interrompe o programa

    print(f'O CPF {cpf_completo} é válido!')
    
else:
    print('Favor, digite um CPF válido com 11 dígitos numéricos.')
    sys.exit()  # Interrompe o programa

print('Muito obrigado pela consulta!')