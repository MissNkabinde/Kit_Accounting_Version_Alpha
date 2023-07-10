import tkinter as tk
from tkinter import messagebox, font


login_window = tk.Tk()
login_window.geometry('925x600+350+100')
login_window.configure(bg='#0d0828')
login_window.title("Login")


def validate_login():
    username = username_entry.get()
    password = password_entry.get()
    login_window.destroy()
    import addClient


def register_button_clicked():
    login_window.destroy()
    import user


def on_entry_click(event):
    if username_entry.get() == "Username":
        username_entry.delete(0, "end")
        username_entry.config(fg="black")


def entry_click(event):
    if password_entry.get() == "Password":
        password_entry.delete(0, "end")
        password_entry.config(fg="black")


def here():
    messagebox.showinfo("OTP has been sent to your email!")


def close_windows():
    login_window.destroy()


# ============================ login content ==========================================================================

bold_font = font.Font(family="CASTELLAR", size=22, weight="bold")
label = tk.Label(login_window, text="User Login", font=bold_font, fg="lime", bg="#0d0828")
label.pack(pady=10)

frame = tk.Frame(login_window, bg='#0d0828')  # Create a frame for center alignment
frame.pack(expand=True)

username_entry = tk.Entry(frame)
username_entry.insert(0, "Username")
username_entry.bind("<FocusIn>", on_entry_click)
username_entry.pack(pady=10)

password_entry = tk.Entry(frame, show="*")
password_entry.insert(0, "Password")
password_entry.bind("<FocusIn>", entry_click)
password_entry.pack(pady=10)  # Added pady to move the entry down

custom_font = ("Cambria", 12)
here_label = tk.Label(frame, text="Forgot Password, click ", fg='white', bg='#0d0828', font=custom_font)
here_label.pack(pady=10)

here_button = tk.Button(frame, text="here", command=here, fg='blue', bg='#0d0828', font=custom_font)
here_button.pack(pady=10)

login_button = tk.Button(frame, text="Login", command=validate_login)
login_button.pack(pady=10)

register_button = tk.Button(frame, text="Register", command=register_button_clicked)
register_button.pack(pady=10)
# ==================================================================================================================

login_window.protocol("WM_DELETE_WINDOW", close_windows)
login_window.mainloop()
