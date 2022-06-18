#Import all the necessary libraries
from sre_parse import State
from tkinter import *
from PIL import Image
from tkinter import messagebox
import random
from datetime import datetime
import sys

def funct():
    #Define the tkinter instance
    win= Toplevel()
    win.title("Daily reward")

    #Define the working of the button
    file="opening_box.gif"

    gems = open("time.txt", "r")
    if gems.read() == "":
        f = open("time.txt", "w")
        f.write(f"0\n0")
        f.close()


    def total_gem():
        gems = open("time.txt", "r")
        next(gems)
        gems = gems.read()
        if gems == "":
            return 0
        return gems

    def my_command():
        gem = random.randint(25, 50)

        now = datetime.now()
        hour = now.strftime("%H")

        #open and read the file after the appending:
        pre_press = open("time.txt", "r")
        pre_press = pre_press.readline()

        if abs(int(hour) - int(pre_press)) == 0:
            button1["state"] = DISABLED
            button2["state"] = DISABLED
            button3["state"] = DISABLED
            messagebox.showerror("","Wait for enough 1 hour to claim gift")

        if abs(int(hour) - int(pre_press)) >= 1:
            if gem >= 49:
                messagebox.showinfo(title="Reward !", message=f"You unbox {gem} gem, that's insane !!")
            else:
                messagebox.showinfo(title="Reward !", message=f"You unbox {gem} gem, nice !!")

            total_gem_now = int(total_gem()) + gem

            f = open("time.txt", "w")
            f.write(f"{hour}\n{total_gem_now}")
            f.close()

            button1["state"] = NORMAL
            button2["state"] = NORMAL
            button3["state"] = NORMAL
    #Import the image using PhotoImage function
    click_btn= PhotoImage(file='images/box_reward.png')

    #Let us create a label for button event
    img_label= Label(image=click_btn)

    #Let us create a dummy button and pass the image
    button1= Button(win, image=click_btn,command= my_command,borderwidth=0)
    button1.grid(column=1, row = 1)

    button2= Button(win, image=click_btn,command= my_command,borderwidth=0)
    button2.grid(column=2, row = 1)

    button3= Button(win, image=click_btn,command= my_command,borderwidth=0)
    button3.grid(column=3, row = 1)

    text= Label(win, text= "Choose 1 for random gem", font=("Arial",20))
    text.grid(column = 2, row = 2)

    win.mainloop()