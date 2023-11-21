from tkinter import *

ws = Tk()
ws.geometry('600x400')
ws.title('tps exam')
ws['bg']='#f2f2f2'

f = ("times bold", 14)

def choose_exam():
    ws.destroy()
    import page3

def exam_bin():
    ws.destroy()
    import pages_bin_user

def exam_bing():
    ws.destroy()
    import pages_bing_user

def exam_mtk():
    ws.destroy()
    import pages_mtk_user

Label(
    ws,
    text="mau belajar apa hari ini?",
    font=f,
    bg='#f2f2f2',
    padx=40,
    pady=30,
).pack()

w = Label(
    ws,
    text="pilih mata pelajaran",
    font= '50')
w.pack()

Button(
    ws,
    text="literasi bahasa indonesia",
    font=f,
    command=exam_bin,
).pack(pady=(20))

Button(
    ws,
    text="penalaran bahasa inggris",
    font=f,
    command=exam_bing,
).pack(pady=(20))

Button(
    ws,
    text="penalaran MTK",
    font=f,
    command=exam_mtk,
).pack(pady=(20))

Button(
    ws,
    text="kembali",
    font= f,
    command=choose_exam
).pack(pady=(90,20))

ws.mainloop()