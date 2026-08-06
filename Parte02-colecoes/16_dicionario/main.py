#dicionario

usuario = {
    'nome': "Fulano",
    'idade': 58,
    'email':"fulano@gmail.com",
    'cpf': "123.456.789-20"
}

#exibir os dados do dicionario
#forma 1
print(f"Nome: {usuario['nome']}")
print(f"Idade: {usuario['idade']}")
print(f"E-mail: {usuario['email']}")
print(f"CPF: {usuario['cpf']}")

print("<><><><><>")
#forma 2
print(f"Nome: {usuario.get('nome')}")
print(f"Idade: {usuario.get('idade')}")
print(f"E-mail: {usuario.get('email')}")
print(f"CPF: {usuario.get('cpf')}")

print("<><><><><>")
#forma 3
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")