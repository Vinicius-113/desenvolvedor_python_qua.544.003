
import json
import os

arquivo_json = "alunos.json"

# Verifica se o arquivo já existe
if os.path.exists(arquivo_json):
    with open(arquivo_json, "r", encoding="utf-8") as arquivo:
        alunos = json.load(arquivo)
else:
    alunos = []

while True:
    print("\n===== CADASTRO DE ALUNO =====")

    nome = input("Digite o nome do aluno: ")

    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    # Calculando a média
    media = (nota1 + nota2 + nota3) / 3

    # Verificando a situação
    if media >= 7:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    # Criando os dados do aluno
    aluno = {
        "nome": nome,
        "nota1": nota1,
        "nota2": nota2,
        "nota3": nota3,
        "media": round(media, 2),
        "situacao": situacao
    }

    # Adicionando o aluno à lista
    alunos.append(aluno)

    # Salvando no arquivo JSON
    with open(arquivo_json, "w", encoding="utf-8") as arquivo:
        json.dump(alunos, arquivo, indent=4, ensure_ascii=False)

    # Mostrando o resultado
    print("\n===== RESULTADO =====")
    print("Aluno:", nome)
    print("Média:", round(media, 2))
    print("Situação:", situacao)

    # Pergunta se deseja cadastrar outro aluno
    resposta = input("\nDeseja cadastrar outro aluno? (s/n): ")

    if resposta.lower() != "s":
        break

print("\nPrograma encerrado!")

