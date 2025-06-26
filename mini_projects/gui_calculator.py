import tkinter as tk

def calculate(e=None):
    num1 = float(en_num1.get())
    num2 = float(en_num2.get())
    if num1 and num2:

        # For addition
        if operation.get() == 'add':
            lbox_res.insert(tk.END, f"{num1} + {num2} = {(num1+num2):.2f}")

        # For subtraction
        if operation.get() == 'sub':
            lbox_res.insert(tk.END, f"{num1} - {num2} = {(num1-num2):.2f}")

        # For multiplication
        if operation.get() == 'mul':
            lbox_res.insert(tk.END, f"{num1} * {num2} = {(num1*num2):.2f}")
        
        # For division
        if operation.get() == 'div':
            if num2 != 0:
                lbox_res.insert(tk.END, f"{num1} / {num2} = {(num1/num2):.2f}")
            else:
                lbox_res.insert(tk.END, f"Division by zero not possible!")


        # Clearing entries
        en_num1.delete(0, tk.END)
        en_num2.delete(0, tk.END)
        

root = tk.Tk()

# Applying window settings
root.title("Calculator")
root.geometry("500x400")

# Creating a main frame
main_frame = tk.Frame(root)
main_frame.pack()

# Creating a frame1
frame1 = tk.Frame(main_frame)
frame1.pack()


# Creating labels
lbl_num1 = tk.Label(frame1, text="Number 1: ")
lbl_num1.grid(row=0, column=0, padx=(0,10))

lbl_num2 = tk.Label(frame1, text="Number 2: ")
lbl_num2.grid(row=1, column=0, padx=(0,10))


# Creating entrys
en_num1 = tk.Entry(frame1, background="light grey")
en_num1.grid(row=0, column=1)

en_num2 = tk.Entry(frame1, background="light grey")
en_num2.grid(row=1, column=1)


#-----------------------END OF FRAME 1-----------------------#


# Creating new frame for buttons and output
frame2 = tk.Frame(main_frame)
frame2.pack(pady=(20, 0))


# Creating radio buttons to display operations
operation = tk.StringVar()
operation.set("add")

rbtn_add = tk.Radiobutton(frame2, text="Addition", variable=operation, value="add", width=15, anchor='w')
rbtn_add.grid(row=0, column=0)

rbtn_sub = tk.Radiobutton(frame2, text="Subtraction", variable=operation, value="sub", width=15, anchor='w')
rbtn_sub.grid(row=0, column=1)

rbtn_mul = tk.Radiobutton(frame2, text="Multiplication", variable=operation, value="mul", width=15, anchor='w')
rbtn_mul.grid(row=1, column=0)

rbtn_div = tk.Radiobutton(frame2, text="Division", variable=operation, value="div", width=15, anchor='w')
rbtn_div.grid(row=1, column=1)


#-----------------------END OF FRAME 2-----------------------#


# creating the 3rd frame for submit button and answer
frame3 = tk.Frame(main_frame)
frame3.pack(pady=(20, 0))


# Creating the calculate button
btn_calc = tk.Button(frame3,text='Calculate', background="grey", command=calculate, width=10, height=3)
btn_calc.grid(row=0, column=0, padx=(0, 10))
btn_calc.bind("<Return>", calculate)

# Creating result label
lbox_res = tk.Listbox(frame3, background="light grey")
lbox_res.grid(row=0, column=1, padx=(10, 0))


# The main loop
root.mainloop()