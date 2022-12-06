from tkinter import *
import requests
from tkinter import messagebox

# -------------interface--------------

window = Tk()
window.title('Deletar')
window.config(background='#60eba5')
font = ('Nimbus Sans [URW ]', 15, 'italic')


# -----------------function-----------------
def delete():
    categoria = str(digite.get())
    id_ = str(digite0.get())

    link = requests.delete(f'https://requisi-10a9f-default-rtdb.firebaseio.com/{categoria}/{id_}.json')


    print(link)
    print(link.json())

    #messagebox.showerror('Erro', 'verifique as informações')

    messagebox.showinfo('OK', 'Requisição deletada com sucesso')

    if str(digite0.get()) == '':
        messagebox.showerror('Erro', 'verifique as informações')
    if str(digite.get()) == '':
        messagebox.showerror('Erro', 'verifique as informações')


# -------------------widgets------------
catetext = Label(window, font=font, bg='#60eba5', text='Itén a ser excluido: ')
catetext.grid(column=0, row=1)
digite = Entry(window)
digite.grid(column=1, row=1)

deletetexte = Label(window, font=font, bg='#60eba5', text='Digite a categoria: ')
deletetexte.grid(column=0, row=2)
digite0 = Entry(window)
digite.grid(column=1, row=2)

botão = Button(window, text='OK', command=delete)
botão.grid(column=0, row=3)

digite0.grid(column=1, row=1)

window.mainloop()
