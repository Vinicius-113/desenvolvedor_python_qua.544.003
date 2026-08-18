import modulo

while True:
    print("\n===== MENU =====")
    print("1 - Limpar o terminal")
    print("2 - Calcular potência")
    print("3 - Volume de um paralelepípedo")
    print("4 - Volume de um cilindro")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        modulo.limpar()

    elif opcao == "2":
        modulo.potencial()

    elif opcao == "3":
        modulo.volume_paralelepipedo()

    elif opcao == "4":
        modulo.volume_cilindrico()

    elif opcao == "5":
        print("Programa encerrado!")
        break

    else:
        print("Opção inválida!")

    input("\nPressione ENTER para continuar...")