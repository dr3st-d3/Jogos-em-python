# Import's.

import tkinter
from tkinter import *
from tkinter import ttk

# Cores que vão ser usadas no jogo.

co0 = "#FFFFFF"
co1 = "#333333"
co2 = "#fcc058"
co3 = "#fff873"
co4 = "#34eb3d"
co5 = "#e85151"
fundo = "#3b3b3b"

# Janela da aplicação.

janela = Tk()
janela.title('PPT')
janela.geometry('260x280')
janela.configure(bg=fundo)

# Divisões da janela.

frame_cima = Frame(janela, width=260, height=100, bg=co1, relief='raised')
frame_cima.grid(row = 0, column = 0, sticky = NW)

frame_baixo = Frame(janela, width=260, height=180, bg=co0, relief='flat')
frame_baixo.grid(row = 1, column = 0, sticky = NW)

# Estilo da janela.

estilo = ttk.Style(janela)
estilo.theme_use('clam')

# Identificação Jogador x Máquina.

player = Label(frame_cima, text='Você', height=1, anchor='center', font=('ivy 10 bold'), bg=co1, fg=co0)
player.place(x=10, y=70)

machine = Label(frame_cima, text='PC', height=1, anchor='center', font=('ivy 10 bold'), bg=co1, fg=co0)
machine.place(x=205, y=70)

# Contador de Pontuação Jogador x Máquina.

player_score = Label(frame_cima, text='0', height=1, anchor='center', font=('ivy 30 bold'), bg=co1, fg=co0)
player_score.place(x=50, y=20)

middle_line = Label(frame_cima, text=':', height=1, anchor='center', font=('ivy 30 bold'), bg=co1, fg=co0)
middle_line.place(x=120, y=20)

machine_score = Label(frame_cima, text='0', height=1, anchor='center', font=('ivy 30 bold'), bg=co1, fg=co0)
machine_score.place(x=180, y=20)

# Linha Marcadora de Pontuação Jogador x Máquina.

player_line = Label(frame_cima, text='', height=10, anchor='center', font=('ivy 10 bold'), bg=co0, fg=co0)
player_line.place(x=0, y=0)

machine_line = Label(frame_cima, text='', height=10, anchor='center', font=('ivy 10 bold'), bg=co0, fg=co0)
machine_line.place(x=255, y=0)

draw_line = Label(frame_cima, text='', width=255, anchor='center', font=('ivy 1 bold'), bg=co0, fg=co0)
draw_line.place(x=0, y=95)

janela.mainloop()