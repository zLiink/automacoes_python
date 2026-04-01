"""
Interface em CTkinter para geração de receituários:
- Botões para criar receituários nos formatos 15x21 e 14x20.
- Abre os scripts correspondentes para processamento e impressão.
"""

import rec15x21
import rec14x20
import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue") 

janela = ctk.CTk()
janela.title("Scripts")
janela.geometry("500x500")

# Receituario 15x21
botao_15x21 = ctk.CTkButton(janela, text="Receituário 15x21", command=rec15x21.executar_receituario)
botao_15x21.pack(pady=10)

# Receituario 10x14
botao_14x20 = ctk.CTkButton(janela, text="Receituario 14x20", command=rec14x20.executar_receituario)
botao_14x20.pack(pady=10)

janela.mainloop()
