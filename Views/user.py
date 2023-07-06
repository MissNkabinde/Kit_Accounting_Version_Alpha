import tkinter as tk
from tkinter import messagebox, font

user_window = tk.Tk()
user_window.geometry('925x500+350+100')
user_window.configure(bg='#0d0828')
user_window.title("User Access")

def user_register():
    name = name_entry.get()
    emailAddress = emailAddress_entry.get()
    password = password_entry.get()
    conf_password = conf_password_entry.get()
    import login


bold_font = font.Font(family="CASTELLAR", size=18, weight="bold")
label = tk.Label(user_window, text="User Registration", font=bold_font, fg="lime", bg="#0d0828")
label.pack(pady=10)


# Center content in the window
frame = tk.Frame(user_window, bg='#0d0828')
frame.pack(expand=True)

name_label = tk.Label(frame, text="Full Name:", font=('bold', 10), fg="white", bg="#0d0828")
name_label.pack(padx=10, pady=10)

name_entry = tk.Entry(frame)
name_entry.pack(padx=10, pady=10)

emailAddress_label = tk.Label(frame, text="Email Address:", font=('bold', 10), fg="white", bg="#0d0828")
emailAddress_label.pack(padx=10, pady=10)

emailAddress_entry = tk.Entry(frame)
emailAddress_entry.pack(padx=10, pady=10)

password_label = tk.Label(frame, text="Password:", font=('bold', 10), fg="white", bg="#0d0828")
password_label.pack(padx=10, pady=10)

password_entry = tk.Entry(frame, show="*")
password_entry.pack(padx=10, pady=10)

conf_password_label = tk.Label(frame, text="Confirm Password:", font=('bold', 10), fg="white", bg="#0d0828")
conf_password_label.pack(padx=10, pady=10)

conf_password_entry = tk.Entry(frame, show="*")
conf_password_entry.pack(padx=10, pady=10)

register_button = tk.Button(frame, text="Register", command=user_register)
register_button.pack(padx=10, pady=10)

def close_windows():
    user_window.destroy()

# Make the window responsive
user_window.pack_propagate(False)

user_window.mainloop()
