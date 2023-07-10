import tkinter as tk
from tkinter import messagebox, font
from tkinter import ttk


def show_login_screen():
    # Stop the progress bar animation
    progressbar.stop()

    # Destroy the loading screen
    loading_screen.destroy()
    import logReg


# ====================================================================================================================

# Create the loading screen
loading_screen = tk.Tk()
loading_screen.geometry('925x600+350+55')
loading_screen.configure(bg='#471f47')
loading_screen.title("Loading Screen")

bold_font = font.Font(family="CASTELLAR", size=30, weight="bold")
label = tk.Label(loading_screen, text="KIT Accounting", font=bold_font, fg="lime", bg="#471f47")
label.pack(pady=150)

label = tk.Label(loading_screen, text="Loading...", font=("Arial", 10), fg="black", bg="#471f47")
label.pack(side="bottom")

style = ttk.Style()
style.configure("TProgressbar", thickness=30)
progressbar = ttk.Progressbar(loading_screen, style="TProgressbar", mode="indeterminate")
progressbar.pack(side="bottom")
progressbar.start()

# After 5 seconds, transition to the landing screen
loading_screen.after(5000, show_login_screen)

# Start the Tkinter event loop
loading_screen.mainloop()
