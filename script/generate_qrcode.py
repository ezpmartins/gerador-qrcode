import qrcode
from tkinter import *
import os
from pathlib import Path

def gerar_qrcode():
    link = entrada_link.get()
    nome_arquivo = entrada_nome.get()
    
    qr = qrcode.make(link)
    
    download_dir = str(Path.home() / "Downloads")
    caminho_completo = os.path.join(download_dir, f"{nome_arquivo}.png")
    
    qr.save(caminho_completo)
    
    mensagem["text"] = f"QR Code salvo em {caminho_completo}"

janela = Tk()
janela.title("Gerador de QR Code")

label_link = Label(janela, text="Link:")
label_link.pack()
entrada_link = Entry(janela)
entrada_link.pack()

label_nome = Label(janela, text="Nome do arquivo:")
label_nome.pack()
entrada_nome = Entry(janela)
entrada_nome.pack()

botao_gerar = Button(janela, text="Gerar QR Code", command=gerar_qrcode)
botao_gerar.pack()

mensagem = Label(janela, text="")
mensagem.pack()

janela.mainloop()