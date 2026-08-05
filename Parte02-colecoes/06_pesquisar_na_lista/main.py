cidades = [
    "Brasilia",
    "Rio de Janeiro",
    "São Paulo",
    "Goiânia",
    "Fortaleza",
    "Manaus"
]

# informar o nome da cidade a ser pesquisado
cidade_pesquisada = input("Informe o nome da cidade a ser pesquisada: ").strip().title()

# retorna o resultado
print(f"{cidade_pesquisada} encontrada." if cidade_pesquisada in cidades else "cidade não encontrada." )    