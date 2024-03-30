import os

saldo = 0.00
quantidade_de_saque_diario = 0
extrato = ''

VALOR_LIMITE_DE_SAQUE = 500.00
LIMITE_DE_QUANTIDADE_DE_SAQUE = 3

def saque(valor):
    global saldo
    global extrato
    global quantidade_de_saque_diario
    if valor > 0:
        if saldo >= valor:
            if valor <= VALOR_LIMITE_DE_SAQUE and quantidade_de_saque_diario < LIMITE_DE_QUANTIDADE_DE_SAQUE:
                saldo -= valor
                quantidade_de_saque_diario = quantidade_de_saque_diario + 1
                print(f'Você realizou um saque de R$ {valor:.2f}')
                print()
                extrato += f'Saque realizado no valor de R$ {valor:.2f}\n'
            else:
                if quantidade_de_saque_diario >= LIMITE_DE_QUANTIDADE_DE_SAQUE:
                    print('Quantidade de saque diário passou do limite')
                    print()
                if valor > VALOR_LIMITE_DE_SAQUE:
                    print('O saque ultrapassou o limite máximo de R$ 500')
                    print()
        else:
            print('Não será possível sacar o dinheiro por falta de saldo')
            print()
    else:
        print('Operação falhou! O valor informado é inválido.')
        print()

def deposito(valor):
    global saldo
    global extrato
    if valor > 0:
        saldo += valor
        print(f'Você realizou um deposito de R$ {valor:.2f}')
        print()
        extrato += f'Depósito realizado no valor de R$ {valor:.2f}\n'
    else:
        print('Operação falhou! O valor informado é inválido.')
        print()

def imprimir_extrato():
    global extrato
    global saldo
    if extrato:
        extrato += f'Saldo total: R$ {saldo:.2f}\n'
        print(extrato)
        extrato = extrato.replace(f'Saldo total: R$ {saldo:.2f}\n', '')
        print()
    else:
        print('Você não possui movimentações em sua conta')
        print()

menu = '''
        Seja bem-vindo ao nosso banco!        

        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair
        
        Selecione uma opcao: '''

while True:
    opcao = input(menu).lower()
    if opcao == 'd':
        os.system('cls')
        valor = float(input('Digite um valor para deposito: '))
        os.system('cls')
        deposito(valor)
        input('Pressione Enter para continuar...')
        os.system('cls')
    elif opcao == 's':
        os.system('cls')
        valor = float(input('Digite um valor para saque: '))
        os.system('cls')
        saque(valor)
        input('Pressione Enter para continuar...')
        os.system('cls')
    elif opcao == 'e':
        os.system('cls')
        imprimir_extrato()
        input('Pressione Enter para continuar...')
        os.system('cls')
    elif opcao == 'q':
        os.system('cls')
        print('Obrigado pela preferência! Volte sempre :)')
        print()
        input('Pressione Enter para sair...')
        os.system('cls')
        break
    else:
        os.system('cls')
        print('Operação inválida! Por favor, selecione novamente a operação desejada.')
        print()
        input('Pressione Enter para continuar...')
        os.system('cls')