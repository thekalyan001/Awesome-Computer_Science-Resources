#importing required modules

import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random
import os

# creating a GUI window
root = tk.Tk()
root.configure(bg="orange")

#Fixing size
root.geometry("650x550")

#adding image to background

C = Canvas(root, bg="blue", height=30, width=30)
filename = PhotoImage(file =  r"C:\Users\VENOM\Desktop\Guess The Number\\guess_no.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

C.pack()

root.title("                                                           ------GUESS THE NUMBER------")

#intialising variable

result = StringVar()
chances = IntVar()
chances1= IntVar()
choice= IntVar()
no=random.randint(1,50)
result.set("Guess A Number From 1 to 50 ")
chances.set(10)
chances1.set(chances.get())

#Function to guess the number

def guess():
  chances1.set(chances.get())
  if chances.get()>0:

    if choice.get() > 50 or choice.get()<0:
      result.set("You  Lost 1 Chance")
      chances.set(chances.get()-1)
      chances1.set(chances.get())
    
    elif no==choice.get():
      result.set("CONGRATULATION YOU WON!!!")
      chances.set(chances.get()-1)
      chances1.set(chances.get())
      
    elif no > choice.get():
      result.set("Your guess was  LOW: Guess a number HIGHER ")
      chances.set(chances.get()-1)
      chances1.set(chances.get())
    elif no < choice.get():
      result.set(
          "Your guess was  HIGH: Guess a number LOWER ")
      chances.set(chances.get()-1)
      chances1.set(chances.get())
  else:
     result.set(
         "GAME OVER YOU LOST!!!")


#For restarting the game  
def restart():
  no=random.randint(1,50)
  result.set("Guess A Number From 1 to 50 ")
  chances.set(10)
  chances1.set(chances.get())

#Function to Choose HELP for better game information

def buttcall():
    messagebox.showinfo("HOW TO PLAY", " 1.Insert a number from 1 to 50 till your chances are left.                                              2.After inserting click on TRY button AND check the number matches or not.                    3.If not check the clue under the TRY button you will see you number is HIGHER or LOWER.                                                          4.Check again.   ")    
    
#To add an Entry box for Typing number

entry1 = Entry(root, textvariable=choice, width=3,
             font=('Helvetica', 50), relief=GROOVE)
entry1.place(relx=0.5, rely=0.3, anchor=CENTER)

entry2 = Entry(root, textvariable=result, width=50,
             font=('Courier', 15), relief=GROOVE)
entry2.place(relx=0.5, rely=0.7, anchor=CENTER)

#to show the user remaining chances chance 
entry3 = Entry(root, text=chances1, width=2,
             font=('Helvetica', 24), relief=GROOVE)
entry3.place(relx=0.61, rely=0.85, anchor=CENTER)

#Adding a label For Displaying The GAME NAME

msg = Label(root, text='Guess A Number From 1 to 50 ',
            font=("BOLD", 25), relief=GROOVE,bg="chartreuse4")
msg.place(relx=0.5, rely=0.09, anchor=CENTER)


#Adding a label For Displaying No of chances left
msg2 = Label(root, text='No Of Chance Left',
             font=("BOLD", 25), relief=GROOVE,)
msg2.place(relx=0.29, rely=0.85, anchor=CENTER)

#Button to Guess the number

try_no = Button(root, width=8, text='GUESS', font=(
    'courier 10 pitch', 25), command=guess, relief=GROOVE,bg="dark slate gray",activebackground="gold")
try_no.place(relx=0.5, rely=0.5, anchor=CENTER)





#f=tk.Frame(window)
frame = tk.Frame(root, width= 80, height = 40)
frame.pack(side = tk.BOTTOM)



#Button  to Exit game
stop = tk.Button( frame,text = 'EXIT', width = 20, fg = 'black',
                   bg = 'red2',activebackground="brown", relief=tk.GROOVE,
                   bd = 0,padx = 10, pady = 10 , command = root.destroy)
stop.pack(side=tk.RIGHT)

#Button to RESTART the game

reset = tk.Button( frame,text = 'RESTART', width = 20, fg = 'black',
                   bg = 'cyan',activebackground="green2", relief=tk.GROOVE ,
                   bd = 0,padx = 10, pady = 10 , command = restart)
reset.pack(side=tk.BOTTOM)

#Button for HELP

but=tk.Button(root, text = 'HELP?', command=buttcall,bg='peach puff',activebackground="turquoise1", 
              relief=tk.GROOVE)
but.place(relx=0.057, rely=0.1, anchor=CENTER)

#Starting the GUI
root.mainloop()








