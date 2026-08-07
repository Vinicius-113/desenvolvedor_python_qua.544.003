# lista de dicionarios
usuarios = [
    {
         'nome': "Fulano",
         'idade': 17,
         'email':"fulano@gmail.com"
    },
    {
        'nome': "caio",
        'idade': 18,
        'email': "caio@gmail.com"
    },
    {


    }
]

for usuario in usuarios:
    for chave, valor in usuario.items():
        print(f"{chave.capitalize()}: {valor}")
    print(f"{'-'*40}")