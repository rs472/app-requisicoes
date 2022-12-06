from tkinter import *
from tkinter import ttk
import sqlite3
import qrcode
from tkinter import messagebox
from datetime import date

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser

# preparação   
window = Tk()
window.geometry('1920x1080')
window.title('Enviar Requisições')
window.config(background='#006494')

data= date.today()
data_texto = data.strftime('%d/%m/%Y')



#Comandos
def openpdf():
    print = webbrowser.open('requisições.pdf')

def pdfcreator():
    c= canvas.Canvas('requisições.pdf')

    Nome = str(digite0.get()) 
    Lote = str(digite4.get())
    Peso = str(digite1.get()) 
    Quantidade = str(digite.get())

    c.setFont('Helvetica-Bold', 24)
    c.drawString(200, 790, 'Ficha: '+ str(data_texto))

    c.setFont('Helvetica-Bold', 18)
    c.drawString(50, 700, 'Nome: ')
    c.drawString(50, 680, 'Lote: ')
    c.drawString(50, 660, 'Peso: ')
    c.drawString(50, 640, 'Quant.: ')
    c.drawString(50, 620, 'Data: ')

    c.setFont('Helvetica', 18)
    c.drawString(110, 700, Nome)
    c.drawString(110, 680, Lote)
    c.drawString(110, 660, Peso)
    c.drawString(113, 640, Quantidade)
    c.drawString(110, 620, data)

    c.showPage()
    c.save()
    openpdf()



def doubleclick(event):

    frame2.selection()
    for n in frame2.selection():
        col1, col2 ,col3, col4 = frame2.item(n , 'values')
        digite0.insert(END, col1)
        digite4.insert(END, col2)
        digite1.insert(END, col3)
        digite.insert(END, col4)


def createbd():
    con = sqlite3.connect("requisiçoes.db")
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS requests(
                Nome CHAR(10) NOT NULL,
                Lote INTERGER(10) NOT NULL,
                Peso INTERGER (10) NOT NULL,
                Quantidade INTERGER (3) NOT NULL,
                Data INTERGER (10) NOT NULL
                       
            );
""")

    Nome = str(digite0.get()) 
    Lote = str(digite4.get())
    Peso = str(digite1.get())  + 'KG'
    Quantidade = str(digite.get())
    Data = str(data_texto)
    

    cur.execute("""INSERT INTO requests(Nome, Lote, Peso, Quantidade, Data)
    VALUES(?, ?, ?, ?, ?)""", (Nome, Lote, Peso, Quantidade, Data))

    con.commit()
    

    img = qrcode.make('Quantidade:' +   Quantidade +   'Peso:' +   Peso + 'Nome:' +
    Nome+   'Lote:' +   Lote)
    img.save ('Requisições '+ Nome)

def puxar():
    frame2.delete(*frame2.get_children())
    con = sqlite3.connect("requisiçoes.db")
    cur = con.cursor()
    Lista = cur.execute("""SELECT Nome, Lote, Peso, Quantidade FROM requests
    ORDER BY Nome ASC; """)

    for i in Lista:
        frame2.insert("", END, values=i)
    

def deletar():
    con = sqlite3.connect("requisiçoes.db")
    cur = con.cursor()
    Del = cur.execute(""" DELETE FROM requests WHERE Nome = ? """,(digite0.get(),))
    con.commit()


    
# Layout
img1 = PhotoImage(file='logo2 py.png')
imagem = Label(window, bg='#006494', image=img1)
imagem.grid(column=0, row=0)

font1 = ('Laksaman', 25, 'bold')
font2 = ('Nimbus Sans [URW ]', 15, 'italic')
font3 = ('Comic Sans MS Regular', 10)

text0 = Label(window, font=font1, bg='#006494', fg='white',text='Requisiçoes')
text0.grid(column=2, row=0)

textinf = Label(window, font='Laksaman 10', bg='#006494', fg='white',text='             Banco de dados:SQLite3')
textinf.place(relx=0, rely=0.1)

text1 = Label(window, font=font2, bg='#006494',fg='white', text='Digite o nome: ')
text1.grid(column=0, row=1)

digite0 = Entry(window)
digite0.grid(column=1, row=1)

text2 = Label(window, font=font2, bg='#006494', fg='white',text='Digite a quantidade: ')
text2.grid(column=2, row=2)

digite = Entry(window)
digite.grid(column=3, row=2)

text3 = Label(window, font=font2, bg='#006494', fg='white',text='Digite o valor do peso: ', )
text3.grid(column=0, row=2)

digite1 = Entry(window)
digite1.grid(column=1, row=2)

text4 = Label(window, font=font2, bg='#006494',fg='white', text='Digite o Lote do produto: ')
text4.grid(column=2, row=1, padx=10, pady=10)

digite4 = Entry(window)
digite4.grid(column=3, row=1)

botao0 = Button(window, font=font3, text='Excluir requisição',bd=4, command=deletar)
botao0.grid(column=0, row=10)

botao = Button(window, font=font3, text='OK', bd=4, command=createbd)
botao.grid(column=3, row=8)

botao = Button(window, font=font3, text='Verificar Requisições',bd=4,
command=puxar)
botao.grid(column=0, row=16)

frame = Label(window, bd = 4, bg='#2d2b2b',highlightbackground='#0064de', highlightthickness = 6)
frame.place(relx=0.06, rely= 0.5, relheight=0.4, relwidth= 0.7)

frame2 = ttk.Treeview(window, height=3, column=('col1, col2, col3, col4, col5'))
frame2.heading('#0', text='')
frame2.heading('#1,', text='Nome')
frame2.heading('#2,', text='Lote')
frame2.heading('#3,', text='Peso')
frame2.heading('#4,', text='Quantidade')



frame2.column('#0', width=3)
frame2.place(relx=0.07, rely=0.52, relheight=0.36, relwidth=0.68)
frame2.bind('<Double-1>', doubleclick)


scroll = Scrollbar(frame2)
scroll.pack(side = RIGHT, fill = Y)


menubar =  Menu(window)
menu1 = Menu(menubar)
menu2 = Menu(menubar)

def Quit(): window.destroy()
def Loguin(): import login

menubar.add_cascade(label='Opções', menu=menu2)
menu2.add_command(label='Novo Login', command=Loguin)
menu2.add_command(label='Gerar relatorio', command=pdfcreator)
menu2.add_command(label='Sair', command=Quit)

  
window.config(menu=menubar)

window.mainloop()


