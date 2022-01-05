n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo  numero: '))
opcao = 0
while opcao!= 5:
    print('''[1] somar
    [2] multiplicar
    [3] maior
    [4] novos numeros
    [5] sair do programa''')
    opcao= int(input('Qual é a sua opção: '))
    if opcao == 1:
        n3 = n1+n2
        print(f'A soma é {n3}')
    elif opcao == 2:
        n3 = n1*n2
        print(f'A multiplicação é {n3}')
    elif opcao == 3:
        if n1>n2:
            print(f'{n1} é o maior número')
        else:
            print(f'{n2} é o maior numero')
    elif opcao == 4:
        n1 = int(input('Primeiro numero: '))
        n2 = int(input('Segundo  numero: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('opçao invalida.Tente novamente')
print('Fim do programa')
