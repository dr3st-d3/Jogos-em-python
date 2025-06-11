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
janela.title('PPT')
janela.geometry('260x280')
janela.configure(bg=fundo)

# Divisões da janela:

frame_cima = Frame(janela, width=260, height=100, bg=co1, relief='raised')
frame_cima.grid(row = 0, column = 0, sticky = NW)

frame_baixo = Frame(janela, width=260, height=180, bg=co0, relief='flat')
frame_baixo.grid(row = 1, column = 0, sticky = NW)

# Estilo da janela:

estilo = ttk.Style(janela)
estilo.theme_use('clam')

# Identificação Jogador x Máquina:

player = Label(frame_cima, text='Você', height=1, anchor='center', font=('ivy 10 bold'), bg=co1, fg=co6)
player.place(x=10, y=70)

machine = Label(frame_cima, text='PC', height=1, anchor='center', font=('ivy 10 bold'), bg=co1, fg=co6)
machine.place(x=205, y=70)

# Contador de Pontuação Jogador x Máquina:

player_score = Label(frame_cima, text='0', height=1, anchor='center', font=('ivy 30 bold'), bg=co1, fg=co6)
player_score.place(x=50, y=20)

middle_line = Label(frame_cima, text=':', height=1, anchor='center', font=('ivy 30 bold'), bg=co1, fg=co6)
middle_line.place(x=120, y=20)

machine_score = Label(frame_cima, text='0', height=1, anchor='center', font=('ivy 30 bold'), bg=co1, fg=co6)
machine_score.place(x=180, y=20)

# Linha Marcadora de Pontuação Jogador x Máquina:

player_line = Label(frame_cima, text='', height=10, anchor='center', font=('ivy 10 bold'), bg=co0, fg=co0)
player_line.place(x=0, y=0)

machine_line = Label(frame_cima, text='', height=10, anchor='center', font=('ivy 10 bold'), bg=co0, fg=co0)
machine_line.place(x=255, y=0)

draw_line = Label(frame_cima, text='', width=255, anchor='center', font=('ivy 1 bold'), bg=co0, fg=co0)
draw_line.place(x=0, y=95)

# Iniciar Jogo:

def iniciar_jogo():
    
    global img_1
    global img_2
    global img_3
    global b_img_1
    global b_img_2
    global b_img_3

    b_play.destroy()

    img_1 = Image.open(os.path.join(caminho_base, 'Pedra.png'))
    img_1 = img_1.resize((50,50))
    img_1 = ImageTk.PhotoImage(img_1)
    b_img_1 = Button(frame_baixo, command=lambda: jogar('Pedra'), width=50, image=img_1, compound=CENTER, bg=co0, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    b_img_1.place(x=15, y=60) 
    
    img_2 = Image.open(os.path.join(caminho_base, 'Papel.png'))
    img_2 = img_2.resize((50,50))
    img_2 = ImageTk.PhotoImage(img_2)
    b_img_2 = Button(frame_baixo, command=lambda: jogar('Papel'), width=50, image=img_2, compound=CENTER, bg=co0, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    b_img_2.place(x=100, y=60) 
    
    img_3 = Image.open(os.path.join(caminho_base, 'Tesoura.png'))
    img_3 = img_3.resize((50,50))
    img_3 = ImageTk.PhotoImage(img_3)
    b_img_3 = Button(frame_baixo, command=lambda: jogar('Tesoura'), width=50, image=img_3, compound=CENTER, bg=co0, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    b_img_3.place(x=185, y=60) 

# Lógica:

pc_move = Label(frame_baixo, text='', height=1, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0)
pc_move.place(x=10, y=10)

global voce
global pc
global rodadas
global p_voce
global p_pc

rodadas = 5
p_voce = 0
p_pc = 0

def jogar(i):
    
    global rodadas
    global p_voce
    global p_pc

    if rodadas > 0:
        print(rodadas)
        opcoes = ['Pedra', 'Papel', 'Tesoura']
        pc = random.choice(opcoes)
        voce = i

        pc_move['text'] = (f'PC jogou: {pc}')
        pc_move['fg'] = co6

        # Casos de Igualdade:
        
        if voce == 'Pedra' and pc == 'Pedra':
            print('Empate')
            print(p_voce, p_pc)
            player_line['bg'] = co0
            machine_line['bg'] = co0
            draw_line['bg'] = co3
            
            p_voce += 5
            p_pc += 5
        
        elif voce == 'Papel' and pc == 'Papel':
            print('Empate')
            print(p_voce, p_pc)
            player_line['bg'] = co0
            machine_line['bg'] = co0
            draw_line['bg'] = co3
            
            p_voce += 5
            p_pc += 5
        
        elif voce == 'Tesoura' and pc == 'Tesoura':
            print('Empate')
            print(p_voce, p_pc)
            player_line['bg'] = co0
            machine_line['bg'] = co0
            draw_line['bg'] = co3
            
            p_voce += 5
            p_pc += 5

        # Casos de Superioridade:
        
        elif voce == 'Pedra' and pc == 'Papel':
            print('Você perdeu')
            print(p_voce, p_pc)
            player_line['bg'] = co5
            machine_line['bg'] = co4
            draw_line['bg'] = co0
            
            p_pc += 10

        elif voce == 'Pedra' and pc == 'Tesoura':
            print('Você ganhou')
            print(p_voce, p_pc)
            player_line['bg'] = co4
            machine_line['bg'] = co5
            draw_line['bg'] = co0
            
            p_voce += 10

        elif voce == 'Papel' and pc == 'Pedra':
            print('Você ganhou')
            print(p_voce, p_pc)
            player_line['bg'] = co4
            machine_line['bg'] = co5
            draw_line['bg'] = co0
            
            p_voce += 10
        
        elif voce == 'Papel' and pc == 'Tesoura':
            print('Você perdeu')
            print(p_voce, p_pc)
            player_line['bg'] = co5
            machine_line['bg'] = co4
            draw_line['bg'] = co0
            
            p_pc += 10

        elif voce == 'Tesoura' and pc == 'Pedra':
            print('Você perdeu')
            print(p_voce, p_pc)
            player_line['bg'] = co5
            machine_line['bg'] = co4
            draw_line['bg'] = co0
            
            p_pc += 10

        elif voce == 'Tesoura' and pc == 'Papel':
            print('Você ganhou')
            print(p_voce, p_pc)
            player_line['bg'] = co4
            machine_line['bg'] = co5
            draw_line['bg'] = co0
            
            p_voce += 10

        # Relação de ganho de pontos:

        player_score['text'] = p_voce
        machine_score['text'] = p_pc

        # Relação de rodadas:

        rodadas -= 1 

    else:
        fim_de_jogo()

# Fim de Jogo:

def fim_de_jogo():
    global rodadas
    global p_voce
    global p_pc

    p_voce = 0
    p_pc = 0
    rodadas = 5

    b_img_1.destroy()
    b_img_2.destroy()
    b_img_3.destroy()

    player_voce = int(player_score['text'])
    machine_pc = int(machine_score['text'])

    if player_voce > machine_pc:
        vencedor = Label(frame_baixo, text='Parabéns você venceu!!', height=1, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co4)
        vencedor.place(x=5, y=70)
        
    elif player_voce == machine_pc:
        vencedor = Label(frame_baixo, text='Empate total, bom jogo.', height=1, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co3)
        vencedor.place(x=5, y=70)
    
    else:
        vencedor = Label(frame_baixo, text='Você perdeu, tente novamente.', height=1, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co5)
        vencedor.place(x=5, y=70)

# Jogar de novo:

    def novo_jogo():
            player_score['text'] = '0'
            machine_score['text'] = '0'
            vencedor.destroy()

            b_playa.destroy()

            iniciar_jogo()
    
    b_playa = Button(frame_baixo, command=novo_jogo, width=30, text='Novo Jogo', bg=fundo, fg=co6, font=('Ivy 10 bold'), anchor=CENTER, relief=RAISED, overrelief=RIDGE)
    b_playa.place(x=5, y=145)

# Botão iniciar:

b_play = Button(frame_baixo, command=iniciar_jogo, width=30, text='Jogar', bg=fundo, fg=co6, font=('Ivy 10 bold'), anchor=CENTER, relief=RAISED, overrelief=RIDGE)
b_play.place(x=5, y=145)

# Loop:

janela.mainloop()
