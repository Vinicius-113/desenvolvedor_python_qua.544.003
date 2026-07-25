# declaração de variaveis

nome = input('Informe seu nome: ').title() 
peso = float(input("Informe seu peso (kg): "))
altura = float(input('Informe sua altura em metros: ').replace(',','.'))

#calculo do imc
imc = peso / (altura ** 2)

# Diagnóstico 
if imc < 18.5:
    diagnostico = 'abaixo do peso'
elif imc < 25:
    diagnostico = 'peso normal'
elif imc < 30:
    diagnostico = 'sobrepeso'
elif imc < 35:
    diagnostico = 'obesidade grau I'
elif imc < 40:
    diagnostico = 'obesidade grau II'
else:
    diagnostico = 'obesidade grau III'

# saida 

print('\n===Resultado===')
print(f'Nome: {nome}')
print(f'IMC: {imc: .2f}')
print(f"Diagnóstico: {diagnostico}")