from tkinter import *
from tkinter import messagebox
from rand import *

global root
global lab_gen
global lablet_y_n
global labnum_y_n
global labsym_y_n
global inlet_y_n
global innum_y_n
global insym_y_n
global en_num_char
global ask_num_char
global button_enter

root = Tk()
root.title("Random Character Generator")
root.geometry("540x300")

def start_layout():
    global lab_gen
    global lablet_y_n
    global labnum_y_n
    global labsym_y_n
    global inlet_y_n
    global innum_y_n
    global insym_y_n
    global en_num_char
    global ask_num_char
    global button_enter
    
    lab_gen = Label(root, text="            ", padx=5, pady=5, bd=0, fg="white")

    labnum_y_n = Label(root, text="Do you need numbers?", padx=5, pady=5, font=("Segoe UI Bold", 13))
    innum_y_n = Entry(root, bd=0, font=("Segoe UI Bold", 13))

    lablet_y_n = Label(root, text="Do you want letters?", padx=0, pady=0, font=("Segoe UI Bold", 13))
    inlet_y_n = Entry(root, bd=0, font=("Segoe UI Bold", 13))

    labsym_y_n = Label(root, text="Do you want symbols?", padx=5, pady=5, font=("Segoe UI Bold", 13))
    insym_y_n = Entry(root, bd=0, font=("Segoe UI Bold", 13))

    en_num_char = Label(root, text="How many characters do you want?", padx=0, pady=0, font=("Segoe UI Bold", 13))
    ask_num_char = Entry(root, bd=0, font=("Segoe UI Bold", 13))

    button_enter = Button(root, text="Enter", bd=0, bg="darkGray", font=("Segoe UI Bold", 12), command=button_en, padx=5, pady=5)

    lab_gen.grid(row=0, column=0, columnspan=2)
    labnum_y_n.grid(row=1, column=0, ipadx=10, ipady=10)
    innum_y_n.grid(row=1, column=1, ipadx=6, ipady=6)
    lablet_y_n.grid(row=2, column=0, ipadx=10, ipady=10)
    inlet_y_n.grid(row=2, column=1, ipadx=6, ipady=6)
    labsym_y_n.grid(row=3, column=0, ipadx=10, ipady=10)
    insym_y_n.grid(row=3, column=1, ipadx=6, ipady=6)
    en_num_char.grid(row=4, column=0, ipadx=10, ipady=10)
    ask_num_char.grid(row=4, column=1, ipadx=6, ipady=6)
    button_enter.grid(row=5, column=0, columnspan=2, ipadx=6, ipady=6)

def button_en():
    global lab_gen
    global root
    lab_gen.grid_forget()
    labnum_y_n.grid_forget()
    innum_y_n.grid_forget()
    lablet_y_n.grid_forget()
    inlet_y_n.grid_forget()
    labsym_y_n.grid_forget()
    insym_y_n.grid_forget()
    button_enter.grid_forget()
    en_num_char.grid_forget()
    ask_num_char.grid_forget()

    if " " in innum_y_n.get():
        print("Iresha")

    try:
        int(ask_num_char.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid Input for number of characters!")
        start_layout()

    if int(ask_num_char.get()) == 70:
        root.geometry("640x350")
    elif int(ask_num_char.get()) == 75:
        root.geometry("700x350")
    elif int(ask_num_char.get()) == 80:
        root.geometry("540x340")
    elif int(ask_num_char.get()) > 90:
        root.geometry("850x350")
    else:
        root.geometry("540x340")


    lab_gen = Label(root, text=generate(insym_y_n.get().lower(), inlet_y_n.get().lower(), innum_y_n.get().lower(), ask_num_char.get()), bg="white", font=("Segoe UI Bold", 13))

    lab_gen.grid(row=0, column=0, columnspan=2, ipadx=10, ipady=10, padx=5, pady=5)
    labnum_y_n.grid(row=1, column=0, ipadx=10, ipady=10)
    innum_y_n.grid(row=1, column=1, ipadx=6, ipady=6)
    lablet_y_n.grid(row=2, column=0, ipadx=10, ipady=10)
    inlet_y_n.grid(row=2, column=1, ipadx=6, ipady=6)
    labsym_y_n.grid(row=3, column=0, ipadx=10, ipady=10)
    insym_y_n.grid(row=3, column=1, ipadx=6, ipady=6)
    en_num_char.grid(row=4, column=0, ipadx=10, ipady=10)
    ask_num_char.grid(row=4, column=1, ipadx=6, ipady=6)
    button_enter.grid(row=5, column=0, columnspan=2, ipadx=6, ipady=6)

start_layout()

root.mainloop()