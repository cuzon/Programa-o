import tkinter as tk #import = importar, tkinter é uma biblioteca, as=como chamar

janela=tk.Tk()


def inserir_texto(x): #def=definition
    texto.insert(1,0,x)

texto=tk.Text(janela,height=2,width=10,font=("Arial 30"))
texto.grid(columnspan=4) #grid para dar forma a algo

botao1=tk.Button(janela,text="1",command=lambda:inserir_texto("1"),height=2,width=2,font=("Arial 15"))
botao1.grid(column=1,row=2)

janela.geometry("400x400") #janela.geometry é pra defenir o tamanho da aba

janela.mainloop() #mainloop é pra rodar a janela