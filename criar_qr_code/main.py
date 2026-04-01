import qrcode

#Config QRcode
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

#Nome QRcode
nome_qr = "meu_QR"

#Link QRcode
qr.add_data("https://www.google.com/?hl=pt_BR")
qr.make(fit=True)

#Cores QRcode
img = qr.make_image(fill_color="#866E00", back_color="#00681F")

#Link pasta para salvar
link_pasta = r"Y:\DESIGNS\Guilherme(Link)\VSCODE\QRcode"

img.save(f"{link_pasta}\{nome_qr}.png")