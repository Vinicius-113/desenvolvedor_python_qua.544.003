import os
def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def maioridade(idade):
    return "É maior de idade." if idade >=18 else "É menor de idade."