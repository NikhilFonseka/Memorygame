#importing modules
from tkinter import *
import random as rand
import time
import csv


#variables for number generation
score = 0
highscore = 0
templist=[]
number = []
num = None
number_amount = 5
#clears the csv file when you open
with open('excelence.csv', mode='w') as excel:

    write = csv.writer(excel)
    write.writerow(["Answer"])

global user_guess
#when the user gets an answer wrong this logs into a file excelence.csv so the user can check back in retrospect, 
#users can check back and see what numbers they are getting wrong, and find patterns in which numbers they are misremembering

def save_to_csv(templist):
    with open('excelence.csv', mode='a') as excelence:
        answer = csv.writer(excelence)
        answer.writerow([templist])
#this is for the countdown timer
def countdown(time_left):
    if time_left > 0:
        timer_label.config(text=f"Time left: {time_left}s")
        root.after(1000, countdown, time_left - 1) 
    else:
        timer_label.config(text="")  
        hide()  

#game is over you restart
def game_over():
    global score, templist, user_guess, number_amount
    user_guess = User_Guess.get()
    templist = ''.join(map(str, templist))
    submitbutton.pack_forget()
    User_Guess.pack_forget()
    go.config(text="Game over:" "\n" f"Correct answer was {templist}")
    go.pack(pady=30)
    score_label.pack()
    score = 0
    generate_button1.pack()
    number_amount = 5
    User_Guess.delete(0, END)
    save_to_csv(templist)
    

#bug fix user submit before number is visible
def submit_button_on():
        User_Guess.bind('<Return>', check)
        submitbutton.config(command=check)
def submit_button_off():
        User_Guess.unbind('<Return>')
        submitbutton.config(command=lambda: None)

#hides the number you can guess it
def hide():
    submit_button_on()
    show_number.pack_forget()
    User_Guess.config(state="normal")  
    User_Guess.delete(0, END)         
    submitbutton.pack(side=BOTTOM, pady=20)
    User_Guess.pack(fill=X, side=BOTTOM, pady=20)

#if you guess correctly the game continues
def continue_game():
    global number_amount
    User_Guess.delete(0, END)
    User_Guess.config(state="disabled") 
    number_amount = number_amount + 1
    submitbutton.pack_forget()
    User_Guess.pack_forget()
    show_number.pack(pady=100)
    generate_number()

#to generate the random number
def generate_number():
    global score
    submit_button_off()
    score_label.config(text=f"Score: {score}")
    global highscore
    if score > highscore:
        highscore = score
        highscore_label.config(text=f"HighScore: {highscore}")

    generate_button1.pack_forget()
    go.pack_forget()
    global templist, number
    frame2.pack_forget()  
    frame3.pack(expand=True, fill=BOTH)
    User_Guess.config(state="disabled")  # Disable the Entry
    templist = []
    number = []
    for i in range(number_amount):
        num = rand.randint(1, 9)
        templist.append(num)
    number.append(templist)
    show_number.config(text=f"{''.join(map(str, templist))}")
    show_number.pack(pady=100)
#timer, changing as the number length increases
    if score >= 3:
        countdown(6)
    elif score >= 2:
        countdown(4)
    elif score >= 1:
        countdown(3)
    else:
        countdown(2)


#checs if your number was right
def check(event=None):
    global score
    guess = User_Guess.get()
    real_num = ''.join(map(str, templist))
    if guess == real_num: 
        score = score+1
        score_label.config(text=f"Score: {score}")
        continue_game()


    else:#if you got it wrong
        game_over()
#so that the user can only enter numbers into the entry
def validate_input(new_text):
    return new_text.isdigit() or new_text == ""
        

#click to go into the frame2
def on_continue_click():
    frame1.pack_forget()  
    frame2.pack(expand=True, fill=BOTH)

#hover effect for buttons 
#continue button on/off
def cb(event):
    continue_button.config(bg="yellow", fg="black", font=("helvetica", 18, "bold"))
def ncb(event):
    continue_button.config(fg="White",bg="gold", font=("helvetica", 16, "bold"))
#generate button on/off
def gb(event):
    generate_button.config(bg="yellow", fg="black", font=("helvetica", 18, "bold"))
def ngb(event):
    generate_button.config(fg="White",bg="gold", font=("helvetica", 16, "bold"))
#submit button button on/off
def sb(event):
    submitbutton.config(bg="yellow", fg="black", font=("helvetica", 16, "bold"))
def nsb(event):
    submitbutton.config(fg="White",bg="gold", font=("helvetica", 16, "bold"))
#generate button for game over hover effect
def sgb(event):
    generate_button1.config(bg="yellow", fg="black", font=("helvetica", 16, "bold"))
def nsgb(event):
    generate_button1.config(fg="White",bg="gold", font=("helvetica", 16, "bold"))




#to run application 
root = Tk()
root.title("Memory Game")
root.geometry("500x400")
root.configure(bg="black")

#for stopping user from entering anything other than a number
validate_cmd = root.register(validate_input)

#creating frame 2
frame2= Frame(root, bg="black")
#frame 1 creation
frame1 = Frame(root, bg="black")
frame1.pack(expand=True,fill=BOTH)

#title head of text
titlelabel = Label(frame1,text="Memory game",font=("helvetica", 45,"bold"), fg="Orange",bg="Black")
titlelabel.pack(pady=10)

#information tells user what the game is
Author = Label(frame1,text="By Nikhil",
    font=("helvetica", 16, "bold"), bg="black", fg="white",wraplength=450)
Author.pack(pady=30)
#Continue button
continue_button = Button(frame1, text="Start game", font=("helvetica", 16, "bold"), fg="White",bg="Gold", command=on_continue_click, padx=20, pady=10,activebackground="white", activeforeground="black" )
continue_button.bind("<Enter>",cb)
continue_button.bind("<Leave>",ncb)
continue_button.pack(side=BOTTOM, pady=20)

#Frame 2
header2 = Label(frame2,text="Are you ready?",font=("helvetica", 26, "bold",),fg="Red",bg="Black")
header2.pack(side=TOP, pady=20)
header = Label(frame2,text="Welcome to the memory game you will be shown a sequence of numbers, you have 5 seconds to remember it, and when the times runs out you have to type it into the box, Good Luck!",
    font=("helvetica", 12, "bold"), bg="black", fg="teal",wraplength=450)
header.pack(pady=30)
reward = Label(frame2,text="First person to reach 9: dont miss out on secret reward",
    font=("helvetica", 10, "bold"), bg="black", fg="darkgreen", wraplength=450)
reward.pack()
#this button generates the randon number
generate_button = Button(frame2,text="Generate random number", font=("helvetica", 16, "bold"), fg="White",bg="Gold", command=generate_number, padx=20, pady=10,activebackground="grey", activeforeground="black" )
generate_button.bind("<Enter>",gb)
generate_button.bind("<Leave>",ngb)
generate_button.pack(side=BOTTOM, pady=20)

#frame 3
frame3 = Frame(root,bg="black")

#this shows you the number so you can remember it
show_number = Label(frame3, text="",font=("helvetica", 30, "bold"),fg="#39FF14",bg="Black")
timer_label = Label(frame3, text="", font=("helvetica", 16, "bold"), fg="red", bg="black")
timer_label.pack(pady=10, side=TOP)
#this is where the user guess it 
User_Guess = Entry(frame3, font=("Arial", 20),validate="key",validatecommand=(validate_cmd, "%P") )
#they can either click this or eneter
submitbutton = Button(frame3,text="submit", font=("helvetica", 16, "bold"),fg="White",bg="Gold", command=check)
submitbutton.bind("<Enter>",sb)
submitbutton.bind("<Leave>",nsb)
#press eneter to guess
User_Guess.bind("<Return>", check)
#score of the user
score_label = Label(frame3, text=f"Score: {score}", font=("helvetica", 16, "bold"),fg="White",bg="Black")
highscore_label = Label(frame3, text=f"High Score: {highscore}", font=("helvetica", 24, "bold"),fg="gold",bg="Black")
highscore_label.pack(side=TOP, pady=10)
score_label.pack(side=TOP, pady=10)
#game over
go = Label(frame3, text="Game over", font=("helvetica", 23, "bold"), bg="black", fg="red")

#generate button and hover effect
generate_button1 = Button(frame3, text="Restart", font=("helvetica", 16, "bold"), fg="White", bg="Gold", command=generate_number, padx=20, pady=10, activebackground="grey", activeforeground="black")
generate_button1.bind("<Enter>",sgb)
generate_button1.bind("<Leave>",nsgb)

#end root/ tkinter 
root=mainloop()
