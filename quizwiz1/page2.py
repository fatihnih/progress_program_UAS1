from tkinter import *

ws = Tk()
ws.geometry('600x400')
ws.title('Halaman Admin')
ws['bg']='#f2f2f2'

f = ("Times bold", 14)
 
def login_page():
    ws.destroy()
    import page1

def buat_soal():
    ws.destroy()
    import buat_soal

Label(
    ws,
    text="HAIII",
    padx=20,
    pady=20,
    bg='#f2f2f2',
    font=f
).pack(expand=True, fill=BOTH)

Button(
    ws, 
    text="Buat Soal", 
    font=f,
    command=buat_soal
    ).pack(pady=20)

Button(
    ws, 
    text="Halaman Login", 
    font=f,
    command=login_page
    ).pack(pady=(80, 20))



ws.mainloop()