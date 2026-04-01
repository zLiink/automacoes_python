import customtkinter as ctk
import clickImpressoes as imp

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

janela = ctk.CTk()
janela.geometry("500x100")
janela.title("Impressões")

loginWeb = ctk.CTkButton(janela, text = "Click Impressões", command=imp.clickImpressoes)
loginWeb.pack(pady=10)

janela.mainloop()

