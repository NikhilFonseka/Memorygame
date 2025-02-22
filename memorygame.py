from tkinter import *
import random as rand
import time
#variables for number generation
score = 0
templist=[]
number = []
num = None
number_amount = 5

def game_over():
    global score
    submitbutton.pack_forget()
    User_Guess.pack_forget()
    go.pack(pady=100)
    score_label.pack(pady=100)
    score = 0
    generate_button.pack(side=BOTTOM, pady=20)

def hide():
    show_number.pack_forget()
    submitbutton.pack(side=BOTTOM, pady=20)
    User_Guess.pack(fill=X, side=BOTTOM, pady=20)


def continue_game():
    global number_amount
    User_Guess.delete(0, END)
    number_amount = number_amount+1
    submitbutton.pack_forget()
    User_Guess.pack_forget()
    show_number.pack(pady=100)
    generate_number()

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


    show_number.config(text=f"{''.join(map(str, templist))}")
    root.after(300, hide)

def check(event=None):
    global score
    guess = User_Guess.get()
    real_num = ''.join(map(str, templist))
    if guess == real_num:
        print("working")
        score = score+1
        score_label.config(text=f"Score: {score}")
        continue_game()
        
        print(score)
    else:
        game_over()
        User_Guess.delete(0, END)

def validate_input(new_text):
    return new_text.isdigit() or new_text == ""
        

#click to go into the frame2
def on_continue_click():
    frame1.pack_forget()  
    frame2.pack(expand=True, fill=BOTH)

#hover effect

def cb(event):
    continue_button.config(bg="yellow", fg="black", font=("helvetica", 18, "bold"))
#hover effect
def ncb(event):
    continue_button.config(fg="White",bg="Black", font=("helvetica", 16, "bold"))

def gb(event):
    generate_button.config(bg="yellow", fg="black", font=("helvetica", 18, "bold"))
def ngb(event):
    generate_button.config(fg="White",bg="Black", font=("helvetica", 16, "bold"))

def sb(event):
    submitbutton.config(bg="yellow", fg="black", font=("helvetica", 16, "bold"))
def nsb(event):
    submitbutton.config(fg="White",bg="Black", font=("helvetica", 16, "bold"))




#to run application 
root = Tk()
root.title("Memory Game")
root.geometry("500x400")
root.configure(bg="black")

validate_cmd = root.register(validate_input)

#creating frame 2
frame2= Frame(root, bg="black")
#frame 1 creation
frame1 = Frame(root, bg="black")
frame1.pack(expand=True,fill=BOTH)

#title head of text
titlelabel = Label(frame1,text="Memory game",font=("helvetica", 30,"bold"), fg="White",bg="Black")
titlelabel.pack()

#information tells user what the game is
header = Label(frame1,text="Welcome to the memory game you will be shown a sequence of numbers, you have 5 seconds to remember it, and when the times runs out you have to type it into the box, Good Luck!",
    font=("helvetica", 12, "bold"), bg="black", fg="teal",wraplength=450)
header.pack(pady=30)

#Continue button
continue_button = Button(frame1, text="Start game", font=("helvetica", 16, "bold"), fg="White",bg="Black", command=on_continue_click, padx=20, pady=10,activebackground="white", activeforeground="black" )
continue_button.bind("<Enter>",cb)
continue_button.bind("<Leave>",ncb)
continue_button.pack(side=BOTTOM, pady=20)

#Frame 2
header2 = Label(frame2,text="Are you ready?",font=("helvetica", 16, "bold",),fg="Red",bg="Black")
header2.pack(side=TOP, pady=20)

generate_button = Button(frame2,text="Generate random number", font=("helvetica", 16, "bold"), fg="White",bg="Black", command=generate_number, padx=20, pady=10,activebackground="grey", activeforeground="black" )
generate_button.bind("<Enter>",gb)
generate_button.bind("<Leave>",ngb)
generate_button.pack(side=BOTTOM, pady=20)

frame3 = Frame(root,bg="black")

show_number = Label(frame3, text="",font=("helvetica", 30, "bold"),fg="White",bg="Black")
show_number.pack(pady=100)

User_Guess = Entry(frame3, font=("Arial", 20),validate="key",validatecommand=(validate_cmd, "%P") )
submitbutton = Button(frame3,text="submit", font=("helvetica", 16, "bold"),fg="White",bg="Black", command=check)
submitbutton.bind("<Enter>",sb)
submitbutton.bind("<Leave>",nsb)

User_Guess.bind("<Return>", check)

score_label = Label(frame3, text=f"Score: {score}", font=("helvetica", 16, "bold"),fg="White",bg="Black")
score_label.pack(side=TOP, pady=10)

go = Label(frame3, text="Game over", font=("helvetica", 25, "bold"), bg="white", fg="black")


root=mainloop()


