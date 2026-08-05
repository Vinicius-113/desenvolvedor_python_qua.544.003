cidades = [
    "Brasilia",
    "Rio de Janeiro",
    "São Paulo",
    "Goiânia",
    "Fortaleza",
    "Manaus"
]

cidade = input("Informe a cidade a ser pesquisada: ").strip().title()

# mostra a posição do item na lista
if cidade in cidades:
    indice = cidades.index(cidade)
    print(f"indice de {cidade} na lista é {indice}.")
else:
    print("cidade não encontrada.")