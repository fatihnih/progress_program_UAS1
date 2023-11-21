from tkinter import *

ws = Tk()
ws.geometry('600x400')
ws.title('Halaman User')
ws['bg']='#f2f2f2'

f = ("Times bold", 14)

def enter_tps():
    ws.destroy()
    import page4

def enter_tlb():
    ws.destroy()
    import page5
 
def login_page():
    ws.destroy()
    import page1

Label(
    ws,
    text="HAIII",
    padx=40,
    pady=30,
    bg='#f2f2f2',
    font=f
).pack()

w = Label(ws, text ='pilih tipe pelajaran', font = "50")  
w.pack() 

Button(
    ws,
    text="TPS",
    font=f,
    command=enter_tps
    ).pack(pady=(40,50))

Button(
    ws,
    text="TLB dan PMTK",
    font=f,
    command=enter_tlb
    ).pack(pady=(10,50))
  
Button(
    ws, 
    text="Halaman Login", 
    font=f,
    command=login_page
    ).pack(pady=(10, 50))

ws.mainloop()