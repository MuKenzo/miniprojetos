'''
Esse projeto verifica se o usuário está realizando uma distribuição correta do salário.
O ideal é que essa distribuição seja da seguinte forma:

- 50% -> Gastos Essenciais: moradia, transporte, alimentação, contas fixas (água e luz).
- 30% -> Lazer: viagem, restaurante, entretenimento.
- 20% -> Investimentos: aposentadoria, previdência privada, investimentos em geral.
'''

import sys

print('---------- CONTROLE FINANCEIRO ----------')
print('')

# Recebe o salário informado pelo usuário
salario = input('Digite o seu salário mensal - R$ ')

# Verifica se o salário é numérico.
if salario.isnumeric():
    # Formata o salário para int
    salario = float(salario)
else:
    print('Favor, digite um salário numérico.')
    sys.exit() # Interrompe o programa

# Recebe os gastos essenciais do usuário
print('Gastos Essenciais: moradia, transporte, alimentação, contas fixas (água e luz).')
gastos_essenciais = input('Digite o valor que é utilizado para gastos essenciais (por mês) - R$ ')

# Verifica se o valor de "gastos_essenciais" é numérico.
if gastos_essenciais.isnumeric():
    # Formata "gastos_essenciais" para int
    gastos_essenciais = float(gastos_essenciais)
else:
    print('Favor, digite um salário numérico.')
    sys.exit() # Interrompe o programa

# Recebe os gastos com lazer do usuário.
print('Lazer: viagem, restaurante, entretenimento.')
lazer = input('Digite o valor que é utilizado para o lazer (por mês) - R$ ')

# Verifica se o valor de "lazer" é numérico.
if lazer.isnumeric():
    # Formata "lazer" para int
    lazer = float(lazer)
else:
    print('Favor, digite um salário numérico.')
    sys.exit() # Interrompe o programa

# Recebe o valor dos investimentos do usuário.
print('Investimentos: aposentadoria, previdência privada, investimentos em geral.')
investimentos = input('Digite o valor que é destinado para investimentos (por mês) - R$ ')

# Verifica se o valor de "investimentos" é numérico.
if investimentos.isnumeric():
    # Formata "investimentos" para int
    investimentos = float(investimentos)
else:
    print('Favor, digite um salário numérico.')
    sys.exit() # Interrompe o programa
    
# Verifica se a soma dos valores corresponde ao salário:
valores = gastos_essenciais + lazer + investimentos
if valores != salario:
    print('A somatória das 3 categorias deve ser igual ao salário. Favor, digite novamente.')
    sys.exit()
else:
    # Verifica se o valor destinado para os gastos essenciais, está dentro do ideal.
    percentual_gastos_essenciais = (gastos_essenciais / salario) * 100
    if percentual_gastos_essenciais <= 50:
        print(f'Do salário de R$ {salario:.2f}, você utiliza R$ {gastos_essenciais:.2f} para os gastos essenciais.')
        print(f'Como esse valor representa {percentual_gastos_essenciais:.2f}% do salário, está dentro do ideal.')
    elif percentual_gastos_essenciais < 100:
        print(f'Do salário de R$ {salario:.2f}, você utiliza R$ {gastos_essenciais:.2f} para os gastos essenciais.')
        print(f'Como esse valor representa {percentual_gastos_essenciais:.2f}% do salário, está fora do ideal. Favor, reavaliar esse gasto.')
    else:
        print(f'Do salário de R$ {salario:.2f}, você utiliza R$ {gastos_essenciais:.2f} para os gastos essenciais.')
        print(f'Como esse valor representa {percentual_gastos_essenciais:.2f}% do salário, você gasta mais do que ganha. Favor, reavaliar esse gasto URGENTE!.')
    
    # Verifica se o valor destinado para o lazer, está dentro do ideal.
    percentual_lazer = (lazer / salario) * 100
    if percentual_lazer <= 30:
        print(f'Do salário de R$ {salario:.2f}, você utiliza R$ {lazer:.2f} para o lazer.')
        print(f'Como esse valor representa {percentual_lazer:.2f}% do salário, está dentro do ideal.')
    elif percentual_lazer < 100:
        print(f'Do salário de R$ {salario:.2f}, você utiliza R$ {lazer:.2f} para o lazer.')
        print(f'Como esse valor representa {percentual_lazer:.2f}% do salário, está fora do ideal. Favor, reavaliar esse gasto.')
    else:
        print(f'Do salário de R$ {salario:.2f}, você utiliza R$ {lazer:.2f} para o lazer.')
        print(f'Como esse valor representa {percentual_lazer:.2f}% do salário, você gasta mais do que ganha. Favor, reavaliar esse gasto URGENTE!.')
    
    # Verifica se o valor destinado para investimentos, está dentro do ideal.
    percentual_investimentos = (investimentos / salario) * 100
    if percentual_investimentos < 10:
        print(f'Do salário de R$ {salario:.2f}, você utiliza R$ {investimentos:.2f} para investimentos.')
        print(f'Como esse valor representa apenas {percentual_investimentos:.2f}% do salário, será necessário reavaliar esse valor.')
    elif percentual_investimentos <= 20:
        print(f'Do salário de R$ {salario:.2f}, você utiliza R$ {investimentos:.2f} para investimentos.')
        print(f'Como esse valor representa {percentual_investimentos:.2f}% do salário, está dentro do ideal.')
    elif percentual_investimentos <= 40:
        print(f'Do salário de R$ {salario:.2f}, você utiliza R$ {investimentos:.2f} para investimentos.')
        print(f'Como esse valor representa {percentual_investimentos:.2f}% do salário, está fora do ideal. No entanto, caso as outras categorias estejam dentro do ideal, investir um valor maior é uma ótima alternativa.')
    elif percentual_investimentos < 100:
        print(f'Do salário de R$ {salario:.2f}, você utiliza R$ {investimentos:.2f} para investimentos.')
        print(f'Como esse valor representa {percentual_investimentos:.2f}% do salário, está fora do ideal. Favor, reavaliar esse valor.')
    else:
        print(f'Do salário de R$ {salario:.2f}, você utiliza R$ {investimentos:.2f} para investimentos.')
        print(f'Como esse valor representa {percentual_investimentos:.2f}% do salário, você investe mais do que ganha. Favor, reavaliar esse investimento URGENTE!.')