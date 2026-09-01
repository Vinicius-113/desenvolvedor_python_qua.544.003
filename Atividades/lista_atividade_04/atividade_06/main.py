
import os
from models import Pessoa, Conta

def limpar():
    os.system("cls" if os.name == "nt" else "clear")


def main():

    print("===== ABERTURA DE CONTA =====")

    # Agência e número da conta já definidos
    agencia = "0001"
    n_conta = "12345-6"

    # Dados preenchidos pelo usuário
    nome = input("Digite seu nome: ")
    cpf = input("Digite seu CPF: ")

    # Saldo inicial
    saldo = float(input("Digite o saldo inicial: R$ "))

    # Criando a pessoa
    pessoa = Pessoa(
        nome=nome,
        cpf=cpf
    )

    # Criando a conta
    conta = Conta(
        agencia=agencia,
        n_conta=n_conta,
        titular=pessoa,
        saldo=saldo
    )

    print("\nConta criada com sucesso!")

    conta.consultar_dados()

    limpar()

    # Menu
    while True:

        print("\n===== MENU =====")
        print("1 - Consultar dados")
        print("2 - Gerar extrato")
        print("3 - Depositar")
        print("4 - Sacar")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":

            conta.consultar_dados()

        elif opcao == "2":

            conta.gerar_extrato()

        elif opcao == "3":

            try:
                valor = float(
                    input("Digite o valor do depósito: R$ ")
                )

                novo_saldo = conta.depositar(valor)

                print(
                    f"Depósito realizado com sucesso!"
                )
                print(
                    f"Saldo atual: R$ {novo_saldo:.2f}"
                )

            except ValueError as erro:
                print(f"Erro: {erro}")

        elif opcao == "4":

            try:
                valor = float(
                    input("Digite o valor do saque: R$ ")
                )

                novo_saldo = conta.sacar(valor)

                print(
                    f"Saque realizado com sucesso!"
                )
                print(
                    f"Saldo atual: R$ {novo_saldo:.2f}"
                )

            except ValueError as erro:
                print(f"Erro: {erro}")

        elif opcao == "5":

            print("Programa encerrado.")
            break

        else:

            print("Opção inválida!")


if __name__ == "__main__":
    main()

