from PIL import Image

imagem = Image.open("apo.jpg")
imagem.save("apo.ico", format="ICO")

print("Ícone convertido com sucesso!")
