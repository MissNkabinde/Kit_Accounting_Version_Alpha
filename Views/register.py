import tkinter as tk
from tkinter import messagebox, font

register_window = tk.Tk()
register_window.geometry('925x600+350+100')
register_window.configure(bg='#0d0828')
register_window.title("register")

def register():
    # Get the values from the entry fields
    companyName = companyName_entry.get()
    companyAddress = companyAddress_entry.get()
    phoneNumber = phoneNumber_entry.get()
    emailAddress = emailAddress_entry.get()
    link = link_entry.get()
    companyLogo = companyLogo_entry.get()

    register_window.destroy()
    import login
def close_windows():
    register_window.destroy()


# ============================ register content ========================================================================
bold_font = font.Font(family="CASTELLAR", size=22, weight="bold")
label = tk.Label(register_window, text="Company Registration", font=bold_font, fg="lime", bg="#0d0828")
label.pack(pady=10)

# Center content in the window
frame = tk.Frame(register_window, bg='#0d0828')
frame.pack(expand=True)

def beautify_entry(entry_widget):
    entry_widget.config(highlightcolor="lime", highlightthickness=2, insertbackground="white")

companyName_label = tk.Label(frame, text="Company Name:", font=('bold', 10), fg="white", bg="#0d0828")
companyName_label.grid(row=0, column=0, pady=5, sticky="e")

companyName_entry = tk.Entry(frame)
companyName_entry.grid(row=0, column=1, pady=5)
beautify_entry(companyName_entry)

companyAddress_label = tk.Label(frame, text="Company Address:", font=('bold', 10), fg="white", bg="#0d0828")
companyAddress_label.grid(row=1, column=0, pady=5, sticky="e")

companyAddress_entry = tk.Entry(frame)
companyAddress_entry.grid(row=1, column=1, pady=5)
beautify_entry(companyAddress_entry)

phoneNumber_label = tk.Label(frame, text="Phone Number:", font=('bold', 10), fg="white", bg="#0d0828")
phoneNumber_label.grid(row=2, column=0, pady=5, sticky="e")

phoneNumber_entry = tk.Entry(frame)
phoneNumber_entry.grid(row=2, column=1, pady=5)
beautify_entry(phoneNumber_entry)

emailAddress_label = tk.Label(frame, text="Email Address:", font=('bold', 10), fg="white", bg="#0d0828")
emailAddress_label.grid(row=3, column=0, pady=5, sticky="e")

emailAddress_entry = tk.Entry(frame)
emailAddress_entry.grid(row=3, column=1, pady=5)
beautify_entry(emailAddress_entry)

link_label = tk.Label(frame, text="Website Link (optional):", font=('bold', 10), fg="white", bg="#0d0828")
link_label.grid(row=4, column=0, pady=5, sticky="e")

link_entry = tk.Entry(frame)
link_entry.grid(row=4, column=1, pady=5)
beautify_entry(link_entry)

companyLogo_label = tk.Label(frame, text="Company Logo:", font=('bold', 10), fg="white", bg="#0d0828")
companyLogo_label.grid(row=5, column=0, pady=5, sticky="e")

companyLogo_entry = tk.Entry(frame)
companyLogo_entry.grid(row=5, column=1, pady=5)
beautify_entry(companyLogo_entry)

register_button = tk.Button(frame, text="Register", command=register, bg="#33ff33", fg="#0d0828",
                            font=('bold', 12), relief=tk.RAISED, highlightbackground="#0d0828",
                            padx=15, pady=8)
register_button.grid(row=6, column=0, columnspan=2, pady=10)

register_window.protocol("WM_DELETE_WINDOW", close_windows)
register_window.mainloop()
