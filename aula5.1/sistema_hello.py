 # desenha tela GUI ( Graphical User InterFace)
import tkinter as tk
from tkinter import messagebox

# exibir o nome da pessoa
def mostrar_mensagem():
    nome = entrada_nome.get()
    messagebox.showinfo("Saudação",f"Olá,{nome} bem vindo!")

# criar uma janela
janela = tk.Tk()
# dar o nome e tamanho
janela.title("Ola Tkinter")
janela.geometry("300x150") # 300 pixels por 150 pixels

# criar o label do input
rotulo_nome = tk.Label(janela,text= "Digite o seu nome:")
rotulo_nome.pack(pady=5) # configurando estilo do texto

# criando campo de texto
entrada_nome =tk.Entry(janela)
entrada_nome.pack(pady=5)

botao =tk.Button(janela, text="Clique aqui", command=mostrar_mensagem,bg="red") 
botao.pack(pady=20)

#inicia o tk
janela.mainloop()