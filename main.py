import tkinter
from tkinter import *
from tkinter import ttk

# cores --------------------------------
co0 = "#FFFFFF"  # white / branca
co1 = "#333333"  # black / preta
co2 = "#fcc058"  # orange / laranja
co3 = "#fff873"  # yellow / amarela
co4 = "#34eb3d"   # green / verde
co5 = "#e85151"   # red / vermelha

fundo = "#3b3b3b"

#Configurando a janela
janela = Tk()
janela.title('')
janela.geometry('260x280') #tamanho da janela
janela.configure(bg=fundo) #cor de fundo

#Dividindo a janela

frame_cima = Frame(janela, width=260, height=100, bg=co1, relief='raised')
frame_cima.grid(row = 0, column = 0, sticky=NW)
frame_baixo = Frame(janela, width=260, height=180, bg=co0, relief='flat')
frame_baixo.grid(row = 1, column = 0, sticky=NW)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

#Configurando o frame cima

#Configurando "Você"
app_1 = Label(frame_cima, text="você", height=1, anchor='center', font=('ivy 10 bold'), bg=co1, fg=co0)
app_1.place(x=25, y=70)

app_1_linha = Label(frame_cima, text="", height=10, anchor='center', font=('ivy 10 bold'), bg=co4, fg=co0)
app_1_linha.place(x=0, y=0)

app_1_pontos = Label(frame_cima, text="0", height=1, anchor='center', font=('ivy 30 bold'), bg=co1, fg=co0)
app_1_pontos.place(x=50, y=20)

#Configurando " : "

app_ = Label(frame_cima, text=":", height=1, anchor='center', font=('ivy 30 bold'), bg=co1, fg=co0)
app_.place(x=125, y=20)


#Configurando "PC"

app_1_pontos = Label(frame_cima, text="0", height=1, anchor='center', font=('ivy 30 bold'), bg=co1, fg=co0)
app_1_pontos.place(x=170, y=20)

app_1 = Label(frame_cima, text="PC", height=1, anchor='center', font=('ivy 10 bold'), bg=co1, fg=co0)
app_1.place(x=205, y=70)

app_1_linha = Label(frame_cima, text="", height=10, anchor='center', font=('ivy 10 bold'), bg=co4, fg=co0)
app_1_linha.place(x=255, y=0)

#Configurando a linha de empate
app_linha = Label(frame_cima, text="", width=255, anchor='center', font=('ivy 1 bold'), bg=co3, fg=co0)
app_linha.place(x=0, y=95)



janela.mainloop() #loop da tela rodando infinaitamente
