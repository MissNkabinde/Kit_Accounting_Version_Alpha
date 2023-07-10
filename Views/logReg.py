import tkinter as tk
from tkinter import messagebox, font


welcome_window = tk.Tk()
welcome_window.geometry('925x600+350+55')
welcome_window.configure(bg='#0d0828')
welcome_window.title("Welcome page")


def register_clicked():
    welcome_window.destroy()
    import user


def login_clicked():
    welcome_window.destroy()
    import login

def close_window():
    welcome_window.destroy()


bold_font = font.Font(family="CASTELLAR", size=22, weight="bold")
label = tk.Label(welcome_window, text="Welcome to KIT Accounting", font=bold_font, fg="lime", bg="#0d0828")
label.pack(pady=10)

login_button = tk.Button(welcome_window, text="Login", command=login_clicked)
login_button.pack(pady=20)

register_button = tk.Button(welcome_window, text="Register", command=register_clicked)
register_button.pack(pady=20)

register_button.mainloop()







