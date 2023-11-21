from tkinter import *
from tkinter import ttk
import data

ws = Tk()
ws.geometry('600x400')
ws.title('Buat Soal')
ws['bg']='#f2f2f2'

e1 = StringVar()
e2 = IntVar()

def save_var():
    materi = e1.get()
    jumlahSoal = e2.get()
    data.simpanVar(materi,jumlahSoal)
    ws.destroy()
    import form_soal

judul = Label(ws, text="BUAT SOALWLEOWLEO")
judul.pack(pady=50)

label1 = ttk.Label(ws, text="Materi:")
label1.pack()

e1 = ttk.Entry(ws)
e1.focus_force()
e1.pack()

label2 = ttk.Label(ws, text="Jumlah Soal:")
label2.pack()

e2 = ttk.Entry(ws) 
e2.focus_force()
e2.pack() 

submit = Button(ws, text="SUBMIT", command=save_var)
submit.pack()


ws.mainloop()