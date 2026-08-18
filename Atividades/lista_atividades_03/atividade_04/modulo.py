import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def potencial():
    base = float(input("Digite a base: "))
    expoente = float(input("Digite o expoente: "))

    resultado = base ** expoente
    print(f"{base} elevado a {expoente} = {resultado}")

def volume_paralelepipedo():
    comprimento = float(input("Digite o comprimento: "))
    largura = float(input("Digite a largura: "))
    altura = float(input("Digite a altura: "))

    volume = comprimento * largura * altura

    print(f"volume do paralelepipedo = {volume}")


def volume_cilindrico():
    raio = float(input("Digite o raio: "))
    altura = float(input("Digite a altura"))

    volume = 3.14159 * (raio ** 2) * altura

    print(f"Volume do cilindro = {volume}")