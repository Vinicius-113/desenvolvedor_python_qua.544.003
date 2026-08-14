import math
import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def area_quadrilatero(b, h):
    return b*h

def area_triangulo(b, h):
    return(b*h)/2

def area_ciculo(r):
    return math.pi*(r**2)

# algoritmo principl
limpar()

while True:
    print("1 - Calcular área do quadrilátero.")
    print("2 - Calcular área do triângulo.")
    print("3 - Calcular área do circulo.")
    print("4 - Sair do programa.")
    opcao = input("Informe a opção desejada: ").strip()
    limpar()
    match opcao:
        case "1":
            b = float(input("Informe o valor da base: ").replace(",","."))
            h = float(input("Informe o valor da altura: ").replace(",","."))
            print(f"Área do quadrilatero é {area_quadrilatero(b, h)}.")
            continue
        case "2":
            b = float(input("Informe o valor da base: ").replace(",","."))
            h = float(input("Informe o valor da altura: ").replace(",","."))
            print(f"Área do triangulo é {area_triangulo(b, h)}.")
            continue
        case "3":
            r = float(input("Informe o valor do raio: ").replace(",","."))
            print(f"Área do circulo é {area_ciculo(r)}.")
            continue
        case "4":
            break
        case _:
            print("opção inválida")
            continue
