# Importações:

import tkinter
from tkinter import *
from tkinter import ttk
import os
from PIL import Image, ImageTk
caminho_base = os.path.dirname(__file__)
import random

# Cores que vão ser usadas no jogo:

co0 = "#4B4B4B"
co1 = "#333333"
co3 = "#fff873"
co4 = "#34eb3d"
co5 = "#e85151"
co6 = "#FFFFFF"
fundo = "#3b3b3b"

# Janela da aplicação:

janela = Tk()
janela.title('QEPK')
janela.geometry('1280x720')
janela.configure(bg=fundo)

# Divisões da janela:

frame_cima = Frame(janela, width=1280, height=360, bg=co1, relief='raised')
frame_cima.grid(row = 0, column = 0, sticky = NW)

frame_baixo = Frame(janela, width=1280, height=361, bg=co0, relief='flat')
frame_baixo.grid(row = 1, column = 0, sticky = NW)

# Estilo da janela:

estilo = ttk.Style(janela)
estilo.theme_use('clam')

# Loop:

janela.mainloop()