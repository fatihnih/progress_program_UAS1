from tkinter import *
from tkinter import ttk
import tkinter as tk
import data

ws = Tk()
ws.geometry('600x400')
ws.title('Buat Soal')
ws['bg']='#f2f2f2'

def function(event):
    # create a label and entry * amount entered
    if entry1.get() == "":
        return
    else:
        i = 1
        while i <= int(entry1.get()):
            label_container = tk.Label(text=f"Container {i}")
            label_container.grid(row=i+1, column=1)

            entry_container = tk.Entry()
            entry_container.grid(row=i+1, column=2)

            jawaban = tk.Checkbutton(text="a)")
            jawaban.grid(row=i+1, column=3)
            jawaban = tk.Checkbutton(text="b)")
            jawaban.grid(row=i+1, column=4)
            jawaban = tk.Checkbutton(text="c)")
            jawaban.grid(row=i+1, column=5)

            i = i + 1

ws.bind("<Return>", function)

########labell###############
judul = tk.Label(text="Judul Soal")
judul.grid(row=0, column=0)

entry2 = tk.Entry()
entry2.grid(row=0, column=1)
entry2.focus()

label_amount = tk.Label(text="Jumlah Soal")
label_amount.grid(row=1, column=0)

entry1 = tk.Entry()
entry1.grid(row=1, column=1)
entry1.focus()

#checkbutton##################
l = tk.Label(ws, bg='#f2f2f2', width=20, text='empty')
#l.pack(pady=20)
 
def print_selection():
    if (var1.get() == 1) & (var2.get() == 0):
        l.config(text='I love Python ')
    elif (var1.get() == 0) & (var2.get() == 1):
        l.config(text='I love C++')
    elif (var1.get() == 0) & (var2.get() == 0):
        l.config(text='I do not anything')
    else:
        l.config(text='I love both')
 
var1 = tk.IntVar()
var2 = tk.IntVar()

c1 = tk.Checkbutton(ws, text='Python',variable=var1, onvalue=1, offvalue=0, command=print_selection)
#c1.pack()
c2 = tk.Checkbutton(ws, text='C++',variable=var2, onvalue=1, offvalue=0, command=print_selection)
#c2.pack()


ws.mainloop()