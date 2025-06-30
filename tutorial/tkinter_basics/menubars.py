import tkinter as tk

root = tk.Tk()

root.title("Menus")
root.geometry("600x350")

main_frame = tk.Frame(root)

menubar = tk.Menu(root)
root.config(menu = menubar)

file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)

root.mainloop()