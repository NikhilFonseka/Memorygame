from tkinter import *
import random as rand

def on_continue_click():
    print("Null")





root = Tk()
root.title = "Memory Game"
root.geometry("500x500")
root.configure(bg="lightgreen")




frame1 = Frame(root,bg="lightgreen")
frame1.pack()
titlelabel = Label(frame1,text="Memory game",font=("Arial", 30,), fg="Yellow")
titlelabel.pack()
header = Label(frame1,text="Welcome to the memory game you will be shown a sequence of numbers, your job is to enter them in the order shown",
    font=("Arial", 15,),
    bg="green", 
    fg="Yellow",
    wraplength=450
               )
header.pack(pady=10)

continue_button = Button(root, text="Continue", font=("Arial", 16), bg="lightblue", fg="black", command=on_continue_click, padx=10, pady=20)

continue_button.pack(pady=170)




root=mainloop()

