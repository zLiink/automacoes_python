"""
Automação para deletar arquivos de uma pasta se já existirem em outra.
Verifica extensões específicas (vídeo e imagem) e pede confirmação antes de apagar.
"""

import os

pasta1 = r"Y:\DESIGNS\Guilherme(Link)\VSCODE\Stories\imgs_teste_pasta_1"
pasta2 = r"Y:\DESIGNS\Guilherme(Link)\VSCODE\Stories\imgs_teste_pasta_2"

extensoes = {
    ".mp4", ".avi", ".mov", ".mkv", ".wmv",
    ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"
}

arquivos_pasta2 = {
    f.lower() for f in os.listdir(pasta2)
    if os.path.splitext(f)[1].lower() in extensoes
}

deletados = 0

for arquivo in os.listdir(pasta1):
    if os.path.splitext(arquivo)[1].lower() in extensoes:
        if arquivo.lower() in arquivos_pasta2:
            caminho = os.path.join(pasta1, arquivo)

            confirm = input(f"Deletar {arquivo}? (s/n): ").lower()
            if confirm == "s":
                os.remove(caminho)
                print(f"Deletado: {arquivo}")
                deletados += 1

print(f"\nTotal deletado: {deletados} arquivo(s)")