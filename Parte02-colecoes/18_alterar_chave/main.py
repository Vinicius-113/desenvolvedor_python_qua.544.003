usuario = {
    'nome': "Fulano",
    'idade': 58,
    'email':"fulano@gmail.com",
    'cpf': "123.456.789-20"
}

#usuario informa a chave que deseja alterar
chave = input("Informe o nome da chave:").strip().lower()

if chave in usuario:
    #usuário informa o novo valor para a chave
    usuario[chave] = input(f"Informe o novo valor para {chave}: ").strip()
    # exibe o dicionario com o novo valor da chave escolhida

    for chave, valor in usuario.items():
        print(f"{chave.capitalize()}: {valor}")
else:
    print("Chave não encontrada.")
