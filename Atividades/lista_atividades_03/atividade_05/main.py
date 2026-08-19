#atividade 05
#Usando recursividade, crie um programa onde o usuário informa um número inteiro e o programa calcula a sequência de Fibonacci até o número informado.





def fibonacci(n):
    return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)

def main():
    n = int(input("Informe um número inteiro: "))
    print(f"O número da sequência de Fibonacci: {fibonacci(n)}")

if __name__ == "__main__":
    main()




#CHAT
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

numero = int(input("Digite um número inteiro: "))

i = 0

print("Sequência de Fibonacci até", numero, ":")

while fibonacci(i) <= numero:
    print(fibonacci(i), end=" ")
    i += 1

