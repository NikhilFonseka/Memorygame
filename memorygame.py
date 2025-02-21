from tkinter import *
import random as rand

def on_continue_click():
    print("Null")





root = Tk()
root.title = "Memory Game"
root.geometry("500x400")
root.configure(bg="silver")




frame1 = Frame(root, bg="silver")
frame1.pack(expand=True,fill=BOTH)

titlelabel = Label(frame1,text="Memory game",font=("helvetica", 30,"bold"), fg="white",bg="silver")
titlelabel.pack()
header = Label(frame1,text="Welcome to the memory game you will be shown a sequence of numbers, your job is to enter them in the order shown",
    font=("helvetica", 12, "bold"),
    bg="silver", 
    fg="#778899",
    
    wraplength=450
               )
header.pack(pady=10)

continue_button = Button(root, text="Continue", font=("helvetica", 16, "bold"), bg="lightblue", fg="black", command=on_continue_click, padx=20, pady=10)

continue_button.pack(pady=20)




root=mainloop()

