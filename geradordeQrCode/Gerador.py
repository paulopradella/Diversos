from  tkinter import* #Código retirado do instagram @python.hub
from tkinter import messagebox
import pyqrcode
import os
janela = Tk()
janela.title("Gerador de QR Code")
#geração code
def gerado():
    if len(assunto.get()) !=0:
        global  meuQr
        meuQr = pyqrcode.create(assunto.get())
        qrImagem = meuQr.xbm(scale=6)
        global imagem
        imagem = BitmapImage(data=qrImagem)
    else:
        messagebox.showinfo("Por favor insira um assunto")
    try:
        mostrarCode()
    except:
        pass
#mostrar código:
def mostrarCode():
    global imagem
    notificationLabel.config(image = imagem)
    subLabel.config(text="QR Code para: " + assunto.get())
def salvar():
    #local onde será salvo os qr codes
    dir = path1 = os.getcwd() +"\\QR Code"
    # criando o local caso não exista
    if not os.path.exists(dir):
        os.makedirs(dir)
    try:
        if len(nome.get())!=0:
            qrImagem = meuQr.png(os.path.join(dir, nome.get() + ".png"), scale=6)
        else:
         messagebox.showinfo("O nome do arquivo não pode ser vazio")
    except:
        messagebox.showinfo("Gere o código primeiro")


lab1 = Label(janela, text= "Entre com o assunto:", font=("Helvettica", 12))
lab1.grid(row=0, column=0, sticky = N + S +E + W)

lab2 = Label(janela, text= "Entre com o nome do arquivo:", font=("Helvettica", 12))
lab2.grid(row=1, column=0, sticky = N + S +E + W)

assunto = StringVar()
assuntoEntry= Entry(janela, textvariable=assunto, font=("Helvettica", 12))
assuntoEntry.grid(row=0, column=1, sticky = N + S +E + W)

nome = StringVar()
nomeEntry= Entry(janela, textvariable=nome, font=("Helvettica", 12))
nomeEntry.grid(row=1, column=1, sticky = N + S +E + W)

createButton = Button(janela, text="Gerar Qr Code",
                      font=("Helvettica", 12), width=15, command=gerado)
createButton.grid(row=0, column=3, sticky = N + S +E + W)
notificationLabel = Label(janela)
notificationLabel.grid(row=2, column=1, sticky = N + S +E + W)

subLabel = Label(janela, text="")
subLabel.grid(row=3, column=1, sticky = N + S +E + W)

showButton = Button(janela, text="Salvar como PNG",
                    font=("Helvettica", 12), width=15, command=salvar)
showButton.grid(row=1, column=3, sticky = N + S +E + W)
# fazendo layout
totalRows = 3
totalCols = 3
for row in range(totalRows + 1):
    janela.grid_rowconfigure(row, weight = 1)
for col in range(totalCols + 1):
    janela.grid_rowconfigure(col, weight = 1)
#looping
janela.mainloop()