# declaracao de variaveis
nome = input('Informe seu nomne: ').title()
idade = int(input('Informe sua idade: '))


# SAIDA DE DADOS CO OPERADOR TERNÁRIO

print(f'{nome} é maior de idade.' if idade>= 18 else f'{nome} é menor de idade.')