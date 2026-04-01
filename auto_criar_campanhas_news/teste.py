import tkinter as tk
from tkinter import messagebox
from datetime import datetime

import pyautogui as pa
import time as tm
import pyperclip as pc

# =========================
# TEMA (cores)
# =========================
BG = "#0F1115"        # fundo geral
PANEL = "#151923"     # painéis
FIELD = "#0F1420"     # inputs
BORDER = "#2A3242"    # bordas
FG = "#E8ECF5"        # texto
MUTED = "#A9B1C6"     # texto secundário
ACCENT = "#7C3AED"    # roxo
ACCENT2 = "#22C55E"   # verde
DANGER = "#EF4444"    # vermelho
BTN = "#242B3B"       # botão padrão
BTN_ACTIVE = "#313A52"

FONT = ("Segoe UI", 10)
FONT_BOLD = ("Segoe UI", 10, "bold")
FONT_TITLE = ("Segoe UI", 12, "bold")


# =========================
# AUTOMAÇÃO
# =========================
def run_automacao(campanhas):
    pa.PAUSE = 0.2
    tm.sleep(3)

    for c in campanhas:
        assunto = c["assunto"]
        complemento_do_assunto = c["complemento"]
        tags = c["tags"]
        id_pagina = c["id_pagina"]
        hora = c["hora"]

        tm.sleep(2)

        # Abrir nova guia
        pa.hotkey("ctrl", "t")
        pa.write("https://login.sendpulse.com/emailservice/tasks/")
        pa.press("enter")
        tm.sleep(12)
        pa.click(x=321, y=299)
        tm.sleep(7)

        pa.click(x=842, y=415)
        tm.sleep(0.4)

        pc.copy("🎈")
        pa.hotkey("ctrl", "v")

        for _ in range(10):
            tm.sleep(0.1)
            pa.press("enter")
            tm.sleep(0.1)
            pa.press("down")

        pa.click(x=1263, y=669)
        tm.sleep(13)

        for _ in range(5):
            pa.press("tab")

        pc.copy(assunto)
        pa.hotkey("ctrl", "v")
        tm.sleep(0.5)

        for _ in range(4):
            pa.press("tab")
            tm.sleep(0.1)

        pa.press("enter")
        tm.sleep(5)

        # Abrindo nova guia para pegar o html da pagina
        pa.hotkey("ctrl", "t")
        pa.write("https://expanssiva.com.br/admin#/emails")
        pa.press("enter")
        tm.sleep(2)
        pa.write(id_pagina)
        pa.press("enter")
        tm.sleep(0.5)

        for _ in range(8):
            pa.press("tab")
            tm.sleep(0.4)

        pa.press("enter")
        tm.sleep(2)

        pa.click(x=411, y=271)
        tm.sleep(2)

        pa.hotkey("ctrl", "u")
        tm.sleep(0.5)
        pa.hotkey("ctrl", "a")
        tm.sleep(0.5)
        pa.hotkey("ctrl", "c")
        tm.sleep(0.5)

        for _ in range(3):
            pa.hotkey("ctrl", "w")
            tm.sleep(0.4)

        pa.click(x=521, y=512)
        tm.sleep(0.4)

        for _ in range(4):
            pa.press("tab")
            tm.sleep(0.1)

        pa.press("enter")
        tm.sleep(0.4)
        pa.press("tab")

        pa.hotkey("ctrl", "v")
        tm.sleep(0.5)

        for _ in range(2):
            pa.press("tab")
            tm.sleep(0.2)

        pa.press("enter")
        tm.sleep(3.5)

        for _ in range(2):
            pa.press("tab")
            tm.sleep(0.2)

        pa.press("enter")
        tm.sleep(2.5)

        for _ in range(6):
            pa.press("tab")
            tm.sleep(0.2)

        pa.press("enter")
        tm.sleep(0.5)
        pc.copy(complemento_do_assunto)
        pa.hotkey("ctrl", "v")
        tm.sleep(0.5)

        pa.press("enter")
        tm.sleep(0.5)

        for _ in range(8):
            pa.press("tab")
            tm.sleep(0.2)

        pa.press("enter")
        tm.sleep(2)

        pa.click(x=782, y=390)
        tm.sleep(0.4)
        pa.press("tab")
        pc.copy(tags)
        pa.hotkey("ctrl", "v")

        for _ in range(10):
            pa.press("tab")
            tm.sleep(0.2)

        pa.press("enter")
        tm.sleep(6)

        pa.press("down", presses=20)
        tm.sleep(0.4)
        pa.click(x=546, y=765)
        tm.sleep(0.4)
        pa.press("tab")
        tm.sleep(0.4)
        pc.copy(hora)
        pa.hotkey("ctrl", "v")
        tm.sleep(0.4)
        pa.click(x=547, y=911)
        tm.sleep(0.4)
        pa.press("down", presses=10)
        tm.sleep(0.4)
        pa.click(x=803, y=726)
        tm.sleep(0.4)
        pa.press("tab")
        tm.sleep(0.4)
        pa.press("6")


# =========================
# UI
# =========================
campanhas = []

def _parse_bloco_5_linhas(texto: str):
    linhas = [l.strip() for l in texto.splitlines() if l.strip()]
    if len(linhas) < 5:
        raise ValueError(
            "Cole as 5 informações em 5 linhas:\n"
            "1) Assunto\n2) Complemento\n3) Tags\n4) ID página\n5) Hora (YYYY-MM-DD HH:MM)"
        )

    assunto, complemento, tags, id_pagina, hora = linhas[:5]

    try:
        datetime.strptime(hora, "%Y-%m-%d %H:%M")
    except ValueError:
        raise ValueError("Hora inválida. Use: YYYY-MM-DD HH:MM (ex: 2026-02-16 07:33)")

    return {"assunto": assunto, "complemento": complemento, "tags": tags, "id_pagina": id_pagina, "hora": hora}

def _set_buttons_state(state: str):
    btn_add.config(state=state)
    btn_remove.config(state=state)
    btn_clear.config(state=state)
    btn_run.config(state=state)

def on_add():
    texto = txt_bloco.get("1.0", "end").strip()
    if not texto:
        messagebox.showerror("Erro", "Cole o bloco com as 5 linhas antes de clicar em +.")
        return
    try:
        campanha = _parse_bloco_5_linhas(texto)
    except Exception as e:
        messagebox.showerror("Erro", str(e))
        return

    campanhas.append(campanha)
    list_assuntos.insert("end", campanha["assunto"] + "   -   " + campanha["hora"])
    lbl_total.config(text=f"Total {len(campanhas)} campanhas")
    txt_bloco.delete("1.0", "end")
    txt_bloco.focus_set()

def on_remove():
    sel = list_assuntos.curselection()
    if not sel:
        return
    i = sel[0]
    list_assuntos.delete(i)
    campanhas.pop(i)
    lbl_total.config(text=f"Total {len(campanhas)} campanhas")

def on_clear():
    campanhas.clear()
    list_assuntos.delete(0, "end")
    lbl_total.config(text="Total 0 campanhas")

def on_run():
    if not campanhas:
        messagebox.showerror("Erro", "Adicione pelo menos 1 campanha.")
        return

    resumo = "\n".join([f"{i+1}) {c['assunto']} — {c['hora']}" for i, c in enumerate(campanhas)])
    ok = messagebox.askyesno("Confirmar", f"Vou executar {len(campanhas)} campanha(s):\n\n{resumo}\n\nContinuar?")
    if not ok:
        return

    _set_buttons_state("disabled")
    root.iconify()
    try:
        run_automacao(campanhas)
        messagebox.showinfo("Concluído", "Automação finalizada.")
    except Exception as e:
        messagebox.showerror("Erro na execução", str(e))
    finally:
        root.deiconify()
        _set_buttons_state("normal")


# =========================
# Construção da janela
# =========================
root = tk.Tk()
root.title("Disparo SendPulse - expanSSiva")
root.configure(bg=BG)

outer = tk.Frame(root, bg=BG, padx=14, pady=14)
outer.pack(fill="both", expand=True)

header = tk.Frame(outer, bg=BG)
header.pack(fill="x", pady=(0, 10))

tk.Label(header, text="Disparo de Campanhas", bg=BG, fg=FG, font=FONT_TITLE).pack(side="left")
tk.Label(header, text="Cole as 5 linhas e clique +", bg=BG, fg=MUTED, font=FONT).pack(side="right")

panel_top = tk.Frame(outer, bg=PANEL, padx=12, pady=12, highlightbackground=BORDER, highlightthickness=1)
panel_top.pack(fill="x")

left_labels = tk.Frame(panel_top, bg=PANEL)
left_labels.pack(side="left", padx=(0, 10), anchor="n")

for t in ["Assunto:", "Complemento:", "Tags:", "id pagina:", "Hora:"]:
    tk.Label(left_labels, text=t, bg=PANEL, fg=MUTED, font=FONT).pack(anchor="w", pady=2)

txt_bloco = tk.Text(
    panel_top,
    width=70,
    height=8,
    bg=FIELD,
    fg=FG,
    insertbackground=FG,
    relief="flat",
    font=FONT,
    highlightbackground=BORDER,
    highlightthickness=1
)
txt_bloco.pack(side="left", fill="x", expand=True)

btn_add = tk.Button(
    panel_top,
    text="+",
    font=("Segoe UI", 22, "bold"),
    width=3,
    bg=ACCENT,
    fg="white",
    activebackground="#5B21B6",
    activeforeground="white",
    relief="flat",
    command=on_add,
    cursor="hand2"
)
btn_add.pack(side="left", padx=10)

panel_mid = tk.Frame(outer, bg=PANEL, padx=12, pady=12, highlightbackground=BORDER, highlightthickness=1)
panel_mid.pack(fill="both", expand=True, pady=10)

tk.Label(panel_mid, text="Campanhas (Assuntos)", bg=PANEL, fg=MUTED, font=FONT_BOLD).pack(anchor="w", pady=(0, 6))

list_assuntos = tk.Listbox(
    panel_mid,
    height=10,
    bg=FIELD,
    fg=FG,
    selectbackground=ACCENT,
    selectforeground="white",
    relief="flat",
    highlightbackground=BORDER,
    highlightthickness=1,
    font=FONT
)

list_assuntos.pack(fill="both", expand=True)

panel_bottom = tk.Frame(outer, bg=BG)
panel_bottom.pack(fill="x")

btn_remove = tk.Button(
    panel_bottom,
    text="Remover selecionado",
    bg=BTN,
    fg=FG,
    activebackground=BTN_ACTIVE,
    activeforeground=FG,
    relief="flat",
    command=on_remove,
    cursor="hand2"
)
btn_remove.pack(side="left")

btn_clear = tk.Button(
    panel_bottom,
    text="Limpar tudo",
    bg=BTN,
    fg=FG,
    activebackground=BTN_ACTIVE,
    activeforeground=FG,
    relief="flat",
    command=on_clear,
    cursor="hand2"
)
btn_clear.pack(side="left", padx=8)

btn_run = tk.Button(
    panel_bottom,
    text="Executar",
    bg=ACCENT2,
    fg="#07110A",
    activebackground="#16A34A",
    activeforeground="#07110A",
    relief="flat",
    height=2,
    padx=18,
    command=on_run,
    cursor="hand2"
)
btn_run.pack(side="right")

lbl_total = tk.Label(outer, text="Total 0 campanhas", bg=BG, fg=MUTED, font=FONT)
lbl_total.pack(anchor="e", pady=(8, 0))

# Exemplo pré-preenchido
txt_bloco.insert(
    "1.0",
    "📢 Comunicado Importante sobre nosso Funcionamento no Carnaval\n"
    "Parceria • Agilidade • Tranquilidade\n"
    "antecipacao_demandas_carnaval_fevereiro_2026\n"
    "7176\n"
    "2026-02-16 07:33\n"
)

root.mainloop()