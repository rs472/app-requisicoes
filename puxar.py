from tkinter import *
import requests
from tkinter import messagebox

# -----------interface---------------

window = Tk()
window.title('Verificar Requisições')
window.config(background='#60eba5')

font1 = ('Laksaman', 25, 'bold')
font2 = ('Nimbus Sans [URW ]', 15, 'italic')
font3 = ('Comic Sans MS Regular', 10)


# ------------function-------------
def buscar():
    id_ = str(digite0.get())

    link = requests.get(f'https://requisi-10a9f-default-rtdb.firebaseio.com/{id_}.json')

    buscar_dic = link.json()

    texto = buscar_dic
    resultado['text'] = texto

    print(link)
    print(link.json())


# -------widgets-------------

text1 = Label(window, font=font2, bg='#60eba5', text='Digite a categoria: ')
text1.grid(column=0, row=1)

digite0 = Entry(window)
digite0.grid(column=1, row=1)

botao0 = Button(window, font=font3, text='ok', command=buscar)
botao0.grid(column=0, row=2)

resultado = Label(window, font=font3, bg='#60eba5', text='')
resultado.grid(column=1, row=3)

window.mainloop()
