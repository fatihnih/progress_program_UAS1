from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image 

def login():
    userid = username_entry.get()
    password = password_entry.get()

    if userid == "admin" and password == "123":
        parent.destroy()
        import page2
    elif userid == "user" and password == "321":
        parent.destroy()
        import page3
    elif userid == "" and password == "":
        messagebox.showerror("Login Failed", "Masukkan username dan password!!")
    elif (userid != "admin" or userid != "user") and (password == "123" or password == "321"):
        messagebox.showerror("Login Failed", "Username salah!!")
    elif (userid == "admin" or userid == "user") and (password != "123" or password != "321"):
        messagebox.showerror("Login Failed", "Password salah!!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

parent = Tk()
parent.title("QuizWizzzz")
parent.geometry("600x400")
parent['bg']='#f2f2f2'
parent.iconbitmap('c:/Users/mifta/OneDrive/Desktop/quizwiz/icon-3.png')

f = ("Times bold", 14)

my_img = ImageTk.PhotoImage(Image.open("icon-3.png" ))
my_label = Label(image=my_img)
my_label.pack(pady=(50,0))

frame = Frame(parent)
frame.pack(pady=40, padx=100, fill="both", expand=True)

username_label = Label(frame, text="Userid:", font=f)
username_label.pack(pady=(12, 0))

username_entry = Entry(frame)
username_entry.pack(pady=(0, 10))

password_label = Label(frame, text="Password:", font=f)
password_label.pack(pady=(12, 0))

password_entry = Entry(frame, show="*") 
password_entry.pack(pady=(0, 10))

login_button = Button(frame, text="Login", command=login, font=f)
login_button.pack(pady=(30, 10))

parent.mainloop()
