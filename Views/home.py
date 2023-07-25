import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk


def create_scrollable_dashboard():
    root = tk.Tk()
    root.geometry('925x600+350+55')
    root.title("KIT Accounting")

    # Create a frame for the header
    header_frame = ttk.Frame(root, height=50, style="Header.TFrame")
    header_frame.pack(side=tk.TOP, fill=tk.X)

    # create a heading
    heading_label = ttk.Label(header_frame, text="Dashboard", style="Heading.TLabel")
    heading_label.pack(side=tk.LEFT, padx=10, pady=10)

    # Create a search bar entry widget
    search_entry = ttk.Entry(header_frame, width=15)
    search_entry.pack(side=tk.RIGHT, padx=(0, 5), pady=10)

    # Create a search button
    search_button = ttk.Button(header_frame, text="Search", width=6)
    search_button.pack(side=tk.RIGHT, pady=10)

    # Create a frame for the sidebar
    sidebar_frame = ttk.Frame(root, width=200, style="Sidebar.TFrame")
    sidebar_frame.pack(side=tk.LEFT, fill=tk.Y)

    # Create a canvas for the main content area
    canvas = tk.Canvas(root)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Add a scrollbar to the canvas
    scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Configure the canvas to use the scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)

    # Create a frame to contain the widgets
    frame = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor=tk.NW)

    # Update the canvas scrollable region when the frame size changes
    def configure_canvas(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    frame.bind("<Configure>", configure_canvas)

    # Bind the canvas scrolling to the mouse wheel
    def scroll_canvas(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    root.bind("<MouseWheel>", scroll_canvas)

    # Configure styles for header and sidebar frames
    root.style = ttk.Style()
    root.style.configure("Header.TFrame", background="gray")
    root.style.configure("Sidebar.TFrame", background="blue")

    # Make the dashboard responsive
    def resize(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    canvas.bind("<Configure>", resize)

    def show_dashboard():
        dashboard_frame.pack(pady=10)
        profile_frame.pack_forget()
        clients_frame.pack_forget()
        item_frame.pack_forget()
        settings_frame.pack_forget()

    def show_profile():
        dashboard_frame.pack_forget()
        profile_frame.pack(pady=10)
        clients_frame.pack_forget()
        item_frame.pack_forget()
        settings_frame.pack_forget()

    def show_clients():
        dashboard_frame.pack_forget()
        profile_frame.pack_forget()
        clients_frame.pack(pady=10)
        item_frame.pack_forget()
        settings_frame.pack_forget()

    def show_item():
        dashboard_frame.pack_forget()
        profile_frame.pack_forget()
        clients_frame.pack_forget()
        item_frame.pack(pady=10)
        settings_frame.pack_forget()

    def show_settings():
        dashboard_frame.pack_forget()
        profile_frame.pack_forget()
        clients_frame.pack_forget()
        item_frame.pack_forget()
        settings_frame.pack(pady=10)

    # Create buttons on the sidebar with commands to switch frames
    dashboard = tk.Button(sidebar_frame, text='Dashboard', fg='white', bg='blue', font=("", 13, "bold"),
                          bd=0, cursor='hand2', activebackground='blue', command=show_dashboard)
    dashboard.place(x=60, y=60)

    profile = tk.Button(sidebar_frame, text='Profile', fg='white', bg='blue', font=("", 13, "bold"),
                        bd=0, cursor='hand2', activebackground='blue', command=show_profile)
    profile.place(x=60, y=100)

    clients = tk.Button(sidebar_frame, text='Clients', fg='white', bg='blue', font=("", 13, "bold"),
                        bd=0, cursor='hand2', activebackground='blue', command=show_clients)
    clients.place(x=60, y=140)

    item = tk.Button(sidebar_frame, text='Item', fg='white', bg='blue', font=("", 13, "bold"),
                     bd=0, cursor='hand2', activebackground='blue', command=show_item)
    item.place(x=60, y=180)

    settings = tk.Button(sidebar_frame, text='Settings', fg='white', bg='blue', font=("", 13, "bold"),
                         bd=0, cursor='hand2', activebackground='blue', command=show_settings)
    settings.place(x=60, y=220)

    # Create frames for each section
    dashboard_frame = ttk.Frame(frame, width=500, height=150)
    profile_frame = ttk.Frame(frame, width=300, height=150)
    clients_frame = ttk.Frame(frame, width=300, height=150)
    item_frame = ttk.Frame(frame, width=600, height=300, style="item.TFrame")
    settings_frame = ttk.Frame(frame, width=200, height=150)

    # Add widgets to each frame (You can customize these frames and widgets as needed)
    dashboard_label = ttk.Label(dashboard_frame, text="Dashboard Frame", font=("Arial", 12))
    dashboard_label.pack(pady=10)

    quote = ttk.Button(dashboard_frame, text="Quotation")
    quote.pack(pady=10)

    for i in range(30):
        label = ttk.Label(dashboard_frame, text=f"Label {i + 1}")
        label.pack(pady=5)

    invoice = ttk.Button(dashboard_frame, text="Invoice")
    invoice.pack(pady=10)

    profile_label = ttk.Label(profile_frame, text="Profile Frame", font=("Arial", 12))
    profile_label.pack(pady=10)

    clients_label = ttk.Label(clients_frame, text="Clients Frame", font=("Arial", 12))
    clients_label.pack(pady=10)

    add_client = ttk.Button(clients_frame, text="Add Client")
    add_client.pack(pady=10)

    item_label = ttk.Label(item_frame, text="Item Frame", font=("Arial", 12))
    item_label.pack(pady=10)

    item = ttk.Button(item_frame, text="Add Item")
    item.pack(pady=10)

    # Create a frame inside the item_frame
    subitem_frame = ttk.Frame(item_frame, width=180, height=120, style="SubItem.TFrame")
    subitem_frame.pack(pady=10)  # Pack the subitem_frame to make it visible

    # Add widgets to the subitem_frame (customize as needed)
    subitem_label = ttk.Label(subitem_frame, text="Subitem Frame")
    subitem_label.pack(pady=10)

    settings_label = ttk.Label(settings_frame, text="Settings Frame", font=("Arial", 12))
    settings_label.pack(pady=10)

    # Call the function to show the dashboard frame initially
    show_dashboard()

    root.style = ttk.Style()
    root.style.configure("Header.TFrame", background="gray")
    root.style.configure("Sidebar.TFrame", background="blue")
    root.style.configure("item.TFrame", background="lime")

    root.mainloop()


# Call the function to create the scrollable dashboard
create_scrollable_dashboard()
