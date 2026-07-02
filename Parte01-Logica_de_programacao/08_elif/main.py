# declaracao de variaveis
nome = input('Informe o nome do aluno:').title()
nota = float(input('Informe a nota do aluno: ').replace(',', '.'))

# verifica se a nota é valida
if nota >= 0 and nota<= 10:
    if nota >=7:
        print(f'{nome} está aprovado.')
    elif nota >= 5:
        print(f'{nome} está de recuperação.')
    else:
        print(f'{nome} está reprovado.')
else:
    print(f'nota de {nome} inválida.')