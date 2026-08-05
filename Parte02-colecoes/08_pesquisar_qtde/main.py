paises = [
   "Brasil",
   "Argentina",
   "Chile",
   "Mécixo",
   "Brasil",
   "Estados Unidos",
   "Irã",
   "Estados Unidos",
   "Argentina",
   "Brasil",
   "Chile"
]

pais = input("informe o país a ser pesquisado: ").strip().title()

# armazenar a quantidade de ocorrência na lista
qtde = paises.count(pais)

print(f"{pais} foi encontrado {qtde} vezes na lista.")
