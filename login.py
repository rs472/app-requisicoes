from tkinter import *
from tkinter import messagebox
import sqlite3


# ------janela------
janela = Tk()
janela.config(background='#006494')
janela.title('Entrar')
        
# ------função---------
def criar_senha():
        con = sqlite3.connect("requisiçoes.db")
        cur = con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS user(
                    Nome CHAR(25) NOT NULL,
                    Senha INTERGER(25) NOT NULL
                           
                );
    """)
        Nome = str(nome1.get())
        Senha = str(senha1.get())

        cur.execute("""INSERT INTO user(Nome, Senha)
        VALUES(?, ?)""", (Nome, Senha))

        con.commit()

credencial= ['rafa', 'skateboard']


def verifica_senha():

    con = sqlite3.connect("requisiçoes.db")
    cur = con.cursor()

    nome = str(nome1.get())
    senha = str(senha1.get())

    cur.execute (f"""SELECT Nome from user WHERE Nome='{nome}' AND Senha= '{senha}';""")
    if not cur.fetchone():  # An empty result evaluates to False.
        print("Login failed")
    else:
        print("Welcome")

    con.commit()
    pass

    
    if credencial[0] == nome and  credencial[1]== senha:    
        messagebox.showinfo('Sucesso', 'Bem vindo ' +credencial[0])
        janela.destroy()
        import app

    elif nome == 'admin' and senha == 'admin':
         messagebox.showinfo('Sucesso', 'Bem vindo Admin')
         janela.destroy()
         import app

        
    else:
        messagebox.showerror('Erro', 'verifique usuario e senha')
    
    
    
# -------Layoult--------

font1 = ('Laksaman', 25, 'bold')
font2 = ('Nimbus Sans [URW ]', 15, 'italic')
font3 = ('Comic Sans MS Regular', 10)

text5 = Label(janela, font=font1, bg='#006494', text='Login', fg='white')
text5.grid(column=1, row=0)

text16 = Label(janela, font=font2, bg='#006494', text='Usuário: ', fg='white')
text16.grid(column=0, row=1)

text25 = Label(janela, font=font2, bg='#006494', text='Senha: ', fg='white')
text25.grid(column=0, row=3)

nome1 = Entry(janela)
nome1.grid(column=1, row=1)

senha1= Entry(janela, show='•')
senha1.grid(column=1, row=3)

botão58 = Button(janela, font=font3, text='Ok',command=verifica_senha)
botão58.grid(column=2)

botão_criar = Button(janela, font=font3, text='Criar Usuario',command=criar_senha)
botão_criar.grid(column=0)

janela.mainloop()
