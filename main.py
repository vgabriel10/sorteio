import tkinter as tk
from tkinter import messagebox as mb
from random import randint
import random
janela = tk.Tk()
janela.geometry('1000x960')
# FUNÇÕES


def sortear_P():
    def sortear_Nomes():
        lista_Nomes.append(label_Lernome.get())
        print(lista_Nomes)
        label_Lernome.delete(0,'end')
    def aleatorio():
        random.shuffle(lista_Nomes)
        a = randint(0,len(lista_Nomes) - 1)
        print(lista_Nomes[a])
        mb.showinfo('Nome Sorteado',f'A pessoa Sorteada foi {lista_Nomes[a]}')
    lista_Nomes = []
    janela2 = tk.Tk()
    janela2.geometry('600x400')
    janela2.title('SORTEIO')
    label_nome = tk.Label(janela2,text='Digite o nome de um participante : ',font='Arial 14')
    label_Lernome = tk.Entry(janela2,width='100')
    botao_Enter = tk.Button(janela2,text='Inserir',font='Arial 10',height='5',width='5',command=sortear_Nomes)
    botao_Sortear = tk.Button(janela2, text='Sortear', font='Arial 10', height='5', width='5',bg='light gray',command=aleatorio)
    # Posicionando Conteudo
    label_nome.place(x=0,y=50)
    label_Lernome.place(x = 300,y=55)
    botao_Enter.place(x=0,y=100)
    botao_Sortear.place(x=100,y=100)
    janela2.mainloop()
def sortear_N():
    def numeros_Aleatorios():
        print('Numero: %s' % (label_Lernumero.get()))
        numero = int(label_Lernumero.get())
        numero_Sorteado = randint(1,numero)
        print(f'O número sorteado foi {numero_Sorteado}')
        mb.showinfo('Número Sorteado',f'O Número Sorteado foi: {numero_Sorteado}')
        label_Lernumero.delete(0,'end')

    janela.quit()
    janela2 = tk.Tk()
    janela2.geometry('600x400')
    janela2.title('SORTEIO')
    # CRIANDO JANELAS
    label_numero = tk.Label(janela2, text='Sorteie um número de 1 até : ', font='Arial 14')
    label_Lernumero = tk.Entry(janela2, width='10')
    tk.Button(janela2, text='Sortear', font='ArialBlack 12', height='5', width='8',command=numeros_Aleatorios).place(x=0, y=100)
    # POSICIONANDO JANELA
    label_numero.place(x=0, y=50)
    label_Lernumero.place(x=250, y=55)
    janela2.mainloop()

#########
# Estou acompanhando os comandos pelos codigos da interface grafica
janela.title('SORTEIO')
label_logo = tk.Label (janela,text = 'Sorteio',font = 'Arial 40', width = 45, bg = 'blue')
label_logo2 = tk.Label(janela,text='Escolha uma Opção',font = 'timesnewroman 30',width = 60,bg = 'gray')
sortear_Pessoas = tk.Button(janela,text='Sortear Pessoas',font = 'Impact 15',width = 30,height=10,bg='light gray',command=sortear_P)
sortear_Numeros = tk.Button(janela,text='Sortear Números',font = 'Impact 15',width = 30,height=10,bg='light gray',command=sortear_N)
# Posicionando Janelas
label_logo.pack()
label_logo2.pack()
sortear_Pessoas.place(x=250,y=150)
sortear_Numeros.place(x=750, y=150)

janela.mainloop()

