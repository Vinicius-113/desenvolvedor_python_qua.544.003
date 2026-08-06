usuario = {
    'nome': "Fulano",
    'idade': 58,
    'email':"fulano@gmail.com",
    'cpf': "123.456.789-20"
}

# adiciona a chave telefone ao dicionário
usuario['telefone' ] = input(f"Informe o telefone de {usuario.get('nome')}: ").strip()

# exibe o dicionário
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")
