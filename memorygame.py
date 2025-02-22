from tkinter import *
import random as rand

templist=[]
number = []
num = None
number_amount = 5

def generate_number():
    templist=[]
    number = []
    for i in range(number_amount):
        num= rand.randint(1, 9)
        templist.append(num)
    number.append(templist)
    print(number)





def on_continue_click():
    frame1.pack_forget()  
    frame2.pack(expand=True, fill=BOTH)

def continue_button_hover(event):
    continue_button.config(bg="yellow", fg="black", font=("helvetica", 18, "bold"))
def no_continue_button_hover(event):
    continue_button.config(bg="lightblue", fg="black", font=("helvetica", 16, "bold"))



root = Tk()
root.title("Memory Game")
root.geometry("500x400")
root.configure(bg="silver")


frame2= Frame(root, bg="lightblue")


frame1 = Frame(root, bg="silver")
frame1.pack(expand=True,fill=BOTH)


titlelabel = Label(frame1,text="Memory game",font=("helvetica", 30,"bold"), fg="white",bg="silver")
titlelabel.pack()
header = Label(frame1,text="Welcome to the memory game you will be shown a sequence of numbers, your job is to enter them in the order shown",
    font=("helvetica", 12, "bold"), bg="silver", fg="teal",wraplength=450)
header.pack(pady=30)

continue_button = Button(frame1, text="Continue", font=("helvetica", 16, "bold"), bg="lightblue", fg="black", command=on_continue_click, padx=20, pady=10,activebackground="white", activeforeground="black" )

continue_button.bind("<Enter>",continue_button_hover)
continue_button.bind("<Leave>",no_continue_button_hover)


continue_button.pack(side=BOTTOM, pady=20)


generate_button = Button(frame2,text="Generate random number", font=("helvetica", 16, "bold"), bg="white", fg="black", command=generate_number, padx=20, pady=10,activebackground="grey", activeforeground="black" )

generate_button.pack(side=BOTTOM, pady=20)

root=mainloop()


