"""
Interface básica de controle com CustomTkinter:
- Painel simples com título e três botões.
- Cada botão executa uma função distinta (ex: iniciar automações).
- Permite iniciar suas automações a partir de uma UI leve e interativa.
"""

import customtkinter as ctk

# ===== CONFIGURAÇÃO =====
ctk.set_appearance_mode("dark")  # dark ou light
ctk.set_default_color_theme("blue")

# ===== FUNÇÕES =====
def funcao1():
    print("Botão 1")

def funcao2():
    print("Botão 2")

def funcao3():
    print("Botão 3")

# ===== JANELA =====
app = ctk.CTk()
app.title("Meu Aplicativo")
app.geometry("500x350")

# ===== TÍTULO =====
titulo = ctk.CTkLabel(app, text="Painel de Controle", font=("Arial", 24))
titulo.pack(pady=20)

# ===== BOTÕES =====
btn1 = ctk.CTkButton(app, text="Executar Ação 1", command=funcao1)
btn1.pack(pady=10)

btn2 = ctk.CTkButton(app, text="Executar Ação 2", command=funcao2)
btn2.pack(pady=10)

btn3 = ctk.CTkButton(app, text="Executar Ação 3", command=funcao3)
btn3.pack(pady=10)

# ===== LOOP =====
app.mainloop()