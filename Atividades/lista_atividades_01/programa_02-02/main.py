# Cadastro do usuário
nome = input("Informe seu nome: ").title()
idade = int(input("Informe sua idade: "))

# Lista de filmes
filmes = {
    1: ("Volta dos que Não Foram", 0),
    2: ("A Roda Quadrada", 12),
    3: ("As Tranças do Rei Careca", 14),
    4: ("Poeira em Alto Mar", 16),
    5: ("A Vingança do Frango Assado", 18)
}

while True:
    print("\n===== CINEMA =====")
    print("Sala 1 - Volta dos que Não Foram (Livre)")
    print("Sala 2 - A Roda Quadrada (12 anos)")
    print("Sala 3 - As Tranças do Rei Careca (14 anos)")
    print("Sala 4 - Poeira em Alto Mar (16 anos)")
    print("Sala 5 - A Vingança do Frango Assado (18 anos)")

    sala = int(input("\nEscolha a sala (1 a 5): "))

    if sala not in filmes:
        print("Sala inválida! Tente novamente.")
        continue

    filme, idade_minima = filmes[sala]

    if idade >= idade_minima:
        print("\nEntrada permitida!")
        print("Bom filme!")

        # Grava o bilhete em um arquivo
        with open("bilhete.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write("===== BILHETE DO CINEMA =====\n")
            arquivo.write(f"Nome: {nome}\n")
            arquivo.write(f"Idade: {idade}\n")
            arquivo.write(f"Filme: {filme}\n")
            arquivo.write(f"Sala: {sala}\n")

        print("Bilhete gravado no arquivo 'bilhete.txt'.")
        break

    else:
        print(f"\nEntrada não permitida!")
        print(f"Este filme é para maiores de {idade_minima} anos.")
        print("Escolha outro filme.")