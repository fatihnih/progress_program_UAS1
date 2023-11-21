from tkinter import *

ws = Tk()
ws.geometry('600x400')
ws.title('tps exam')
ws['bg']='#f2f2f2'

f = ("times bold", 14)

def choose_exam():
    ws.destroy()
    import page3

def exam_kpu():
    ws.destroy()
    import pages_kpu

def exam_kk():
    ws.destroy()
    import pages_kk

def exam_ppu():
    ws.destroy()
    import pages_ppu

def exam_kbm():
    ws.destroy()
    import pages_kbm

Label(
    ws,
    text="mau belajar apa hari ini?",
    font=f,
    bg='#f2f2f2',
    padx=40,
    pady=10,
).pack()

w = Label(
    ws,
    text="pilih mata pelajaran",
    font= '50')
w.pack(pady=10)

Button(
    ws,
    text="kemampuan penalaran umum",
    font=f,
    command=exam_kpu
).pack(pady=(10))

Button(
    ws,
    text="kemampuan kuantitatif",
    font=f,
    command=exam_kk
).pack(pady=(10))

Button(
    ws,
    text="pengetahuan dan penalaran umum",
    font=f,
    command=exam_ppu
).pack(pady=(10))

Button(
    ws,
    text="kemampuan memahami bacaan dan menulis",
    font=f,
    command=exam_kbm
).pack(pady=(10))

Button(
    ws,
    text="kembali",
    font= f,
    command=choose_exam
).pack(pady=(30,20))

ws.mainloop()