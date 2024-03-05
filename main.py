import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random
# Cores
cor_0 = '#FFFFFF' #white
cor_1 = '#333333'  #braco
cor_2 = '#fcc058' #laranja
cor_4 ='#3297a8' #axul
cor_5 ='#fff873' #amarelo
cor_6 ='#fcc058' #laranja
cor_7='#e85151' #varmelho
cor_8 ='#34eb3d' # verde
fundo = '#3b3b3b'

# Variaveis

pontucao_voce = 0
pontucao_pc = 0
rodadas = 5

#configurando a janela
janela = Tk()
janela.title('')
janela.geometry('260x280')
janela.configure(bg= fundo)

# dividino a janela

frame_cima = Frame(janela, width=260, height=100, bg=cor_1, relief='raised')
frame_cima.grid(row=0, column= 0, sticky=NW)
frame_baixo = Frame(janela, width=260, height=300, bg=cor_0, relief='flat')
frame_baixo.grid(row=1, column= 0, sticky=NW)

app_1 = Label(frame_cima, text="Você", height=1, anchor='center', font=('Ivy 10 bold'), bg=cor_1, fg=cor_0)
app_1.place(x=25, y=70)

app_1_linha = Label(frame_cima, text="", height=10, anchor='center', font=('Ivy 10 bold'), bg=cor_0, fg=cor_0)
app_1_linha.place(x=0, y=0)

app_1_pontos = Label(frame_cima, text="0", height=1, anchor='center', font=('Ivy 30 bold'), bg=cor_1, fg=cor_0)
app_1_pontos.place(x=50, y=20)
app_ = Label(frame_cima, text=":", height=1, anchor='center', font=('Ivy 30 bold'), bg=cor_1, fg=cor_0)
app_.place(x=125, y=20)


app_2_pontos = Label(frame_cima, text="0", height=1, anchor='center', font=('Ivy 30 bold'), bg=cor_1, fg=cor_0)
app_2_pontos.place(x=170, y=20)

app_2 =  Label(frame_cima, text="PC", height=1, anchor='center', font=('Ivy 10 bold'), bg=cor_1, fg=cor_0)
app_2.place(x=205, y=70)

app_2_linha = Label(frame_cima, text="", height=10, anchor='center', font=('Ivy 10 bold'), bg=cor_0, fg=cor_0)
app_2_linha.place(x=254, y=0)

app_emp_linha = Label(frame_cima, text="", width=255, anchor='center', font=('Ivy 1 bold'), bg=cor_0, fg=cor_0)
app_emp_linha.place(x=0, y=95)


app_pc = Label(frame_baixo, text="", height=1, anchor='center', font=('Ivy 10 bold'), bg=cor_0, fg=cor_0)
app_pc.place(x=190, y=10)
estilo = ttk.Style(janela)
estilo.theme_use('clam')




# funçao iniciar jogo
def iniciar_jogo():
    global icon_pedra
    global icon_papel
    global icon_tesoura
    global botao_pedra
    global botao_papel
    global botao_tesoura

    botao_jogar.destroy()

    # Botão Pedra
    icon_pedra = Image.open('imagens_projeto/mao_pedra.png')
    icon_pedra = icon_pedra.resize((50,50), Image.ADAPTIVE)
    icon_pedra = ImageTk.PhotoImage(icon_pedra)
    botao_pedra = Button(frame_baixo,command=lambda: jogar('Pedra'), width=50, image=icon_pedra, compound=CENTER, bg= cor_0, fg= cor_0, font=('Ivy 10 bold'),
                            anchor=CENTER, relief=FLAT)
    botao_pedra.place(x=10, y= 60)

    # Botão Papel
    icon_papel = Image.open('imagens_projeto/mao_papel.png')
    icon_papel = icon_papel.resize((50,50), Image.ADAPTIVE)
    icon_papel = ImageTk.PhotoImage(icon_papel)
    botao_papel = Button(frame_baixo,command=lambda: jogar('Papel'), width=50, image=icon_papel, compound=CENTER, bg= cor_0, fg= cor_0, font=('Ivy 10 bold'),
                            anchor=CENTER, relief=FLAT)
    botao_papel.place(x=90, y= 60)

    # Botão Tesoura
    icon_tesoura = Image.open('imagens_projeto/mao_tesoura.png')
    icon_tesoura = icon_tesoura.resize((50,50), Image.ADAPTIVE)
    icon_tesoura = ImageTk.PhotoImage(icon_tesoura)
    botao_tesoura = Button(frame_baixo,command=lambda: jogar('Tesoura'), width=50, image=icon_tesoura, compound=CENTER, bg= cor_0, fg= cor_0, font=('Ivy 10 bold'),
                            anchor=CENTER, relief=FLAT)
    botao_tesoura.place(x=180, y= 60)



# funçao logica do jogo
def jogar(i):
    global pontucao_voce
    global pontucao_pc
    global rodadas 

    if rodadas > 0:
        print(rodadas)
        opcoes_pc = ['Pedra', 'Papel', 'Tesoura']
        pc = random.choice(opcoes_pc)
        voce = i

        app_pc['text'] = pc
        app_pc['fg'] = cor_1

        if voce == 'Pedra' and pc == 'Pedra':
            print('Empate')
            app_1_linha['bg'] = cor_0
            app_2_linha['bg'] = cor_0
            app_emp_linha['bg'] = cor_5

        elif voce == 'Papel' and pc == 'Papel':
            print('Empate')
            app_1_linha['bg'] = cor_0
            app_2_linha['bg'] = cor_0
            app_emp_linha['bg'] = cor_5

        elif voce == 'Tesoura' and pc == 'Tesoura':
            print('Empate')
            app_1_linha['bg'] = cor_0
            app_2_linha['bg'] = cor_0
            app_emp_linha['bg'] = cor_5

        elif voce == 'Pedra' and pc == 'Papel':
            print('Pc ganhou')
            app_1_linha['bg'] = cor_0
            app_2_linha['bg'] = cor_8
            app_emp_linha['bg'] = cor_0

            pontucao_pc += 10

        
        elif voce == 'Pedra' and pc == 'Tesoura':
            print('Voce ganhou')
            app_1_linha['bg'] = cor_8
            app_2_linha['bg'] = cor_0
            app_emp_linha['bg'] = cor_0

            pontucao_voce += 10

        
        elif voce == 'Papel' and pc == 'Pedra':
            print('Voce ganhou')
            app_1_linha['bg'] = cor_8
            app_2_linha['bg'] = cor_0
            app_emp_linha['bg'] = cor_0

            pontucao_voce += 10

        
        elif voce == 'Papel' and pc == 'Tesoura':
            print('Pc ganhou')
            app_1_linha['bg'] = cor_0
            app_2_linha['bg'] = cor_8
            app_emp_linha['bg'] = cor_0

            pontucao_pc += 10

        
        elif voce == 'Tesoura' and pc == 'Papel':
            print('Voce ganhou')
            app_1_linha['bg'] = cor_8
            app_2_linha['bg'] = cor_0
            app_emp_linha['bg'] = cor_0

            pontucao_voce += 10
        
        
        elif voce == 'Tesoura' and pc == 'Pedra':
            print('Pc ganhou')
            app_1_linha['bg'] = cor_0
            app_2_linha['bg'] = cor_8
            app_emp_linha['bg'] = cor_0

            pontucao_pc += 10

        # atualizando pontuação
        app_1_pontos['text'] = pontucao_voce
        app_2_pontos['text'] = pontucao_pc

        # atualizando o numero de rodadas
        rodadas -= 1

    else:

        # chamando a função terminar
        app_1_pontos['text'] = pontucao_voce
        app_2_pontos['text'] = pontucao_pc
        fim_do_jogo()



# Botão Jogar
botao_jogar = Button(frame_baixo, command=iniciar_jogo, width=30, text='Jogar', bg= fundo, fg= cor_0, font=('Ivy 10 bold'),
                      anchor=CENTER, relief=RAISED, overrelief=RIDGE)
botao_jogar.place(x=5, y= 151)


# funçao terminar jogo
def fim_do_jogo():
    global pontucao_voce
    global pontucao_pc
    global rodadas 

    # reiniciando as variaveis em zero
    pontucao_voce = 0
    pontucao_pc = 0
    rodadas = 5


    # destruindo os butoes de opções
    botao_pedra.destroy()
    botao_papel.destroy()
    botao_tesoura.destroy()
    botao_jogar.destroy()

    # Definindo o Vencedor
    jogador_voce = int(app_1_pontos['text'])
    jogador_pc = int(app_2_pontos['text'])

    if jogador_voce > jogador_pc:
        app_vencedor = Label(frame_baixo, text="Você é o Vencedor", height=1, anchor='center', font=('Ivy 10 bold'), bg=cor_0, fg=cor_8)
        app_vencedor.place(x=5, y=60)
    elif jogador_pc > jogador_voce:
        app_vencedor = Label(frame_baixo, text="PC é o Vencedor", height=1, anchor='center', font=('Ivy 10 bold'), bg=cor_0, fg=cor_7)
        app_vencedor.place(x=5, y=60)
    else:
        app_vencedor = Label(frame_baixo, text="Empate", height=1, anchor='center', font=('Ivy 10 bold'), bg=cor_0, fg=cor_5)
        app_vencedor.place(x=5, y=60)

    


     # jogar de novo
    def jogar_de_novo():
        app_1_pontos['text'] = '0'
        app_2_pontos['text'] = '0'
        app_vencedor.destroy()
        
        botao_jogar_denovo.destroy()
            #botao_jogar_denovo.destroy()

        iniciar_jogo()

    botao_jogar_denovo = Button(frame_baixo, command=jogar_de_novo, width=30, text='Jogar de novo', bg= fundo, fg= cor_0, font=('Ivy 10 bold'),
                      anchor=CENTER, relief=RAISED, overrelief=RIDGE)
    botao_jogar_denovo.place(x=5, y= 151)




janela.mainloop()
