from models import Carro

def main():
    carro = Carro(modelo="",potencia=520)

    carro.modelo = input("Informe o modelo do carro: ")
    #carro.potencia = int(input("Informe a potencia do motor: "))

    print(carro.detalhes())
    



if __name__ == "__main__":
    main()