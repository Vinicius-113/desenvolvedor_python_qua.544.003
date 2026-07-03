# tratamento de exceção
try:
    # usuario informa numero inteiro
    n = int(input('Informe um número inteiro: '))

    # laco de repetição
    while n >=0:
        print(n)
        n -= 1
except:
    print('Não foi possível exibir a contagem.')