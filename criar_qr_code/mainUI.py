"""
Gerador de QR Code com interface Tkinter:
- Permite inserir texto ou link.
- Configura versão, tamanho, borda e cores.
- Salva o QR Code gerado em PNG.
"""

import qrcode
import tkinter as tk
from tkinter import filedialog, colorchooser, messagebox

def escolher_cor_qr():
    cor = colorchooser.askcolor()[1]
    if cor:
        entrada_cor_qr.delete(0, tk.END)
        entrada_cor_qr.insert(0, cor)

def escolher_cor_fundo():
    cor = colorchooser.askcolor()[1]
    if cor:
        entrada_cor_bg.delete(0, tk.END)
        entrada_cor_bg.insert(0, cor)

def gerar_qrcode():
    dados = entrada_dados.get()
    versao = int(entrada_versao.get())
    tamanho = int(entrada_tamanho.get())
    borda = int(entrada_borda.get())
    cor_qr = entrada_cor_qr.get()
    cor_bg = entrada_cor_bg.get()

    if not dados:
        messagebox.showwarning("Aviso", "Digite um texto ou link.")
        return

    caminho = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG", "*.png")]
    )

    if not caminho:
        return

    qr = qrcode.QRCode(
        version=versao,
        box_size=tamanho,
        border=borda
    )

    qr.add_data(dados)
    qr.make(fit=True)

    img = qr.make_image(fill_color=cor_qr, back_color=cor_bg)
    img.save(caminho)

    messagebox.showinfo("Sucesso", "QR Code gerado com sucesso!")

janela = tk.Tk()
janela.title("Gerador de QR Code")
janela.geometry("420x320")

tk.Label(janela, text="Texto / Link").pack()
entrada_dados = tk.Entry(janela, width=50)
entrada_dados.pack(pady=5)

tk.Label(janela, text="Versão do QR (1-40)").pack()
entrada_versao = tk.Entry(janela)
entrada_versao.insert(0, "1")
entrada_versao.pack()

tk.Label(janela, text="Tamanho dos blocos (box_size)").pack()
entrada_tamanho = tk.Entry(janela)
entrada_tamanho.insert(0, "10")
entrada_tamanho.pack()

tk.Label(janela, text="Borda").pack()
entrada_borda = tk.Entry(janela)
entrada_borda.insert(0, "5")
entrada_borda.pack()

tk.Label(janela, text="Cor do QR").pack()
frame_cor_qr = tk.Frame(janela)
frame_cor_qr.pack()

entrada_cor_qr = tk.Entry(frame_cor_qr)
entrada_cor_qr.insert(0, "#000000")
entrada_cor_qr.pack(side=tk.LEFT)

tk.Button(frame_cor_qr, text="Escolher", command=escolher_cor_qr).pack(side=tk.LEFT)

tk.Label(janela, text="Cor de Fundo").pack()
frame_cor_bg = tk.Frame(janela)
frame_cor_bg.pack()

entrada_cor_bg = tk.Entry(frame_cor_bg)
entrada_cor_bg.insert(0, "#FFFFFF")
entrada_cor_bg.pack(side=tk.LEFT)

tk.Button(frame_cor_bg, text="Escolher", command=escolher_cor_fundo).pack(side=tk.LEFT)

tk.Button(
    janela,
    text="Gerar QR Code",
    command=gerar_qrcode,
    bg="#4CAF50",
    fg="white",
    height=2
).pack(pady=15)

janela.mainloop()