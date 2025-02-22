from tkinter import *
import random as rand

 

def on_continue_click():
    frame1.pack_forget()  # Hide the first frame
    frame2.pack(expand=True, fill=BOTH)

def continue_button_hover(event):
    continue_button.config(bg="yellow", fg="black", font=("helvetica", 18, "bold"))
def no_continue_button_hover(event):
    continue_button.config(bg="lightblue", fg="black", font=("helvetica", 16, "bold"))



root = Tk()
root.title = ("Memory Game")
root.geometry("500x400")
root.configure(bg="silver")



frame2= Frame(root, bg="babyblue")

frame1 = Frame(root, bg="silver")
frame1.pack(expand=True,fill=BOTH)

titlelabel = Label(frame1,text="Memory game",font=("helvetica", 30,"bold"), fg="white",bg="silver")
titlelabel.pack()
header = Label(frame1,text="Welcome to the memory game you will be shown a sequence of numbers, your job is to enter them in the order shown",
    font=("helvetica", 12, "bold"), bg="silver", fg="#778899",wraplength=450)
header.pack(pady=10)

continue_button = Button(frame1, text="Continue", font=("helvetica", 16, "bold"), bg="lightblue", fg="black", command=on_continue_click, padx=20, pady=10,activebackground="white", activeforeground="black" )

continue_button.bind("<Enter>",continue_button_hover)
continue_button.bind("<Leave>",no_continue_button_hover)


continue_button.pack(side=BOTTOM, pady=20)


generate_button = Button(frame2,"Generate random number")

root=mainloop()

