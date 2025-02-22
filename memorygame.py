from tkinter import *
import random as rand
import time
#variables for number generation
templist=[]
number = []
num = None
number_amount = 5
def hide():
    show_number.pack_forget()
    submitbutton.pack(side=BOTTOM, pady=20)
    User_Guess.pack(fill=X, side=BOTTOM, pady=20)


    
#to generate the random number
def generate_number():
    global templist, number
    frame2.pack_forget()  
    frame3.pack(expand=True, fill=BOTH)
    templist=[]
    number = []
    for i in range(number_amount):
        num= rand.randint(1, 9)
        templist.append(num)
    number.append(templist)
    print(number)
    show_number.config(text=f"{''.join(map(str, templist))}")
    root.after(1500, hide)

def check():
    guess = User_Guess.get()
    real_num = ''.join(map(str, templist))
    if guess == real_num:
        print("working")
    else:
        print("broken")

    
    


#click to go into the frame2
def on_continue_click():
    frame1.pack_forget()  
    frame2.pack(expand=True, fill=BOTH)

#hover effect
def continue_button_hover(event):
    continue_button.config(bg="yellow", fg="black", font=("helvetica", 18, "bold"))
#hover effect
def no_continue_button_hover(event):
    continue_button.config(bg="lightblue", fg="black", font=("helvetica", 16, "bold"))

#to run application 
root = Tk()
root.title("Memory Game")
root.geometry("500x400")
root.configure(bg="silver")

#creating frame 2
frame2= Frame(root, bg="lightblue")
#frame 1 creation
frame1 = Frame(root, bg="silver")
frame1.pack(expand=True,fill=BOTH)

#title head of text
titlelabel = Label(frame1,text="Memory game",font=("helvetica", 30,"bold"), fg="white",bg="silver")
titlelabel.pack()

#information tells user what the game is
header = Label(frame1,text="Welcome to the memory game you will be shown a sequence of numbers, you have 5 seconds to remember it, and when the times runs out you have to type it into the box, Good Luck!",
    font=("helvetica", 12, "bold"), bg="silver", fg="teal",wraplength=450)
header.pack(pady=30)

#Continue button
continue_button = Button(frame1, text="Start game", font=("helvetica", 16, "bold"), bg="lightblue", fg="black", command=on_continue_click, padx=20, pady=10,activebackground="white", activeforeground="black" )
continue_button.bind("<Enter>",continue_button_hover)
continue_button.bind("<Leave>",no_continue_button_hover)
continue_button.pack(side=BOTTOM, pady=20)

#Frame 2
header2 = Label(frame2,text="Are you ready?",font=("helvetica", 16, "bold",))
header2.pack(side=TOP, pady=20)

generate_button = Button(frame2,text="Generate random number", font=("helvetica", 16, "bold"), bg="white", fg="black", command=generate_number, padx=20, pady=10,activebackground="grey", activeforeground="black" )
generate_button.pack(side=BOTTOM, pady=20)

frame3 = Frame(root,bg="lightblue")

show_number = Label(frame3, text="",font=("helvetica", 25, "bold"),fg="White",bg="Black")
show_number.pack(pady=100)

User_Guess = Entry(frame3, font=("Arial", 20) )
submitbutton = Button(frame3,text="submit", font=("helvetica", 16, "bold"), bg="lightblue", fg="black", command=check)
root=mainloop()


