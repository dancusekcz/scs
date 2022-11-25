# to do list:
# tutorial on first run
# password read algorytm, that saves every password to a unique file, that counts how much passwords is saved and with that information shows the right number of passwords
# to-do algorytm, that saves users to-do list to a file and loads it everytime with all the things that were set before. add remove function to remove the exact goal
# info window with all info about the app, creator and source code github

import tkinter as tk
from tkinter import *
from pathlib import Path
from random import seed, randint
from tkinter.filedialog import asksaveasfile
import os
from PIL import ImageTk, Image

seed(1)

# main app window
def mainapploop():
    global win5

    win5= tk.Tk()
    win5.title("Security and Control System")
    win5.geometry("350x350")
    
    label2 = tk.Label(win5, text="Security and Control System - Main Menu")
    label2.grid(row=0, column=5)

    label = tk.Label(win5, text="Reset pin:")
    label.grid(row=2, column=5, padx=50)

    button = tk.Button(win5, text="Reset pin", command=resetpin, width=8)
    button.grid(row=3, column=5, pady=20, padx=50)

    button2 = tk.Button(win5, text="Passwords", command=password, width=10)
    button2.grid(row=1, column=0, pady=20, )

    button3 = tk.Button(win5, text="Notes", command=notes, width=10)
    button3.grid(row=2, column=0, pady=25,)

    button3 = tk.Button(win5, text="Recovery", command=recover, width=10)
    button3.grid(row=3, column=0, pady=1, )

    button4 = tk.Button(win5, text="Info", command=info, width=10)
    button4.grid(row=5, column=0, pady=20, )

    button5 = tk.Button(win5, text="To Do", command=todo, width=10)
    button5.grid(row=4, column=0, pady=20, )

    button6 = tk.Button(win5, text="Secret", command=martinpin, width=10)
    button6.grid(row=5, column=5, pady=20, )

    win5.mainloop()

def martinpin():
    global entry1
    global winn

    winn = tk.Tk()
    winn.title("Enter secret pin")
    winn.geometry("200x100")

    text1 = tk.Label(winn, text="Enter number between 0 and 50:")
    text1.pack()

    entry1 = tk.Entry(winn)
    entry1.pack()

    button1 = tk.Button(winn, text="Enter", command=secretpin)
    button1.pack()

    winn.mainloop()

def tryagain():
    wi.destroy()
    
def error():
    global wi

    wi = tk.Tk()
    wi.title("Error")
    wi.geometry("200x50")

    text1 = tk.Label(wi, text="Wrong pin!")
    text1.pack()

    button1 = tk.Button(wi, text="Ok", command=tryagain)
    button1.pack()

    wi.mainloop()
    

def secretpin():
    x = "26"

    if entry1.get() == x:
        winn.destroy()
        martin()
        
        print("Valid secret pin")
    else:
        print("Wrong secret pin")


def martin():
    global win9

    win5.destroy()

    win9 = tk.Tk()
    win9.title("Martin je babrak")
    win9.geometry("1000x800")

    label = tk.Label(win9, text="Martin je babrak")
    label.pack()

    button = tk.Button(win9, text="Ok", command=ok)
    button.pack(pady=10)

    img = ImageTk.PhotoImage(Image.open("scs\martyn.png"))

    martin = Label(win9, image = img)
    martin.pack()

    win9.mainloop()

def ok():
    win9.destroy()

    mainapploop()


def password():
    global email
    global username
    global pwd1
    global pwd

    pwd = tk.Tk()
    pwd.title("Password manager")
    pwd.geometry("800x100")

    text1 = tk.Label(pwd, text="Enter email, username and password")
    text1.grid(row=0)

    email = tk.Entry(pwd)
    email.grid(row=1, column=1, padx=20)

    username = tk.Entry(pwd)
    username.grid(row=1, column=2, padx=20)

    pwd1 = tk.Entry(pwd)
    pwd1.grid(row=1, column=3, padx=20)

    button1 = tk.Button(pwd, text="Enter", command=savepwd)
    button1.grid(row=2)
    
    button12 = tk.Button(pwd, text="Read pwds", command=mainloop3)
    button12.grid(row=3)

    pwd.mainloop()

def savepwd():
    with open("pwds.scs", "a") as f:
        f.write(email.get() + " " + username.get() + " " + pwd1.get() + "\n")

def verifypin2():
    print("Checking the pin")

    x = textbox2.get()

    pin = open("scs\pintest.scs")

    for line in pin:
        if x == line:
            win3.destroy()

            read()
        else:
            error()

def mainloop3():
    global textbox2
    global win3

    win3 = tk.Tk()
    win3.title("SCS Pin")
    win3.geometry("200x100")
    
    label = tk.Label(win3, text="Enter your pin:")
    label.pack()

    textbox2 = tk.Entry(win3, width=10)
    textbox2.pack(pady=10)

    button = tk.Button(win3, text="Enter", command=verifypin2)
    button.pack(pady=10)

    win3.mainloop()


def read():
    global recovery

    print(os.path.abspath("pwds.scs"))

    recovery = tk.Tk()
    recovery.geometry("300x100")
    recovery.title("Recovery pin path")

    path1 = tk.Label(recovery, text=os.path.abspath("pwds.scs"))
    path1.pack()

    button1 = tk.Button(recovery, text="Ok", command=ok1)
    button1.pack(pady=10)

    recovery.mainloop()
    

# note editor loop
def notes():
    global textbox6
    global winq

    winq = tk.Tk()
    winq.title("Notes")
    winq.geometry("400x550")
    
    label = tk.Label(winq, text="Notes")
    label.pack()

    textbox6 = tk.Text(winq)
    textbox6.pack(pady=10, ipadx=20, ipady=20)

    button = tk.Button(winq, text="Save", command=savenote)
    button.pack(pady=10)

    winq.mainloop()

# system to save the note
def savenote():
    with open("scsnotefile.txt", "w") as f:
        f.write(textbox6.get(1.0, END))
        print("File saved at: " + os.path.abspath("scsnotefile.txt"))

def recover():
    global recovery

    print(os.path.abspath("test123.scs"))

    recovery = tk.Tk()
    recovery.geometry("300x100")
    recovery.title("Recovery pin path")

    path1 = tk.Label(recovery, text=os.path.abspath("test123.scs"))
    path1.pack()

    button1 = tk.Button(recovery, text="Ok", command=ok1)
    button1.pack(pady=10)

    recovery.mainloop()

def ok1():
    recovery.destroy()

def info():
    pass

def todo():
    pass

# pin creation
def mainloop1():
    global textbox1
    global win

    win = tk.Tk()
    win.title("SCS Pin")
    win.geometry("400x100")
    
    label = tk.Label(win, text="Create your pin:")
    label.pack()

    textbox1 = tk.Entry(win, width=10)
    textbox1.pack(pady=10)

    button = tk.Button(win, text="Enter", command=enterpin)
    button.pack(pady=10)

    win.mainloop()


# login with pin
def mainloop2():
    global textbox2
    global win3

    win3 = tk.Tk()
    win3.title("SCS Pin")
    win3.geometry("200x100")
    
    label = tk.Label(win3, text="Enter your pin:")
    label.pack()

    textbox2 = tk.Entry(win3, width=10)
    textbox2.pack(pady=10)

    button = tk.Button(win3, text="Enter", command=verifypin)
    button.pack(pady=10)

    win3.mainloop()

# reset pin function
def resetpin():
    global textbox3
    global win2

    win2= tk.Tk()
    win2.title("Reset pin:")
    win2.geometry("400x100")
    
    label = tk.Label(win2, text="Enter recovery key")
    label.pack()

    textbox3 = tk.Entry(win2, width=10)
    textbox3.pack(pady=10)

    button = tk.Button(win2, text="Enter", command=recoveryresetpin)
    button.pack(pady=10)

    win2.mainloop()

# window where you type the recovery key, that was created at the first app start
def recoveryresetpin():
    x = textbox3.get()

    pin = open("test123.scs")

    for line in pin:
        if x == line:
            print("Valid recovery key")

            pinpopup()
        else:
            print("Wrong recovery")

# here you type new pin after typing the recovery key
def pinpopup():
    global popup
    global textbox4

    popup = tk.Tk()
    popup.title("Enter new pin:")
    popup.geometry("200x100")

    textbox4 = tk.Entry(popup, width=10)
    textbox4.pack(pady=10)

    button1 = tk.Button(popup, text="Enter", command=confirmresetpin)
    button1.pack()

    popup.mainloop()

# reset pin system
def confirmresetpin():
    with open("pintest.scs", "w") as f:
        print(textbox4.get())
        f.write(textbox4.get())

        f.close()

        popup.destroy()
        win2.destroy()

# pin file creation
def enterpin():
    with open("pintest.scs", "w") as f:
        print(textbox1.get())
        f.write(textbox1.get())

        f.close()

        win.destroy()

# verifying the typed pin
def verifypin():
    print("Checking the pin")

    x = textbox2.get()

    pin = open("pintest.scs")

    for line in pin:
        if x == line:
            win3.destroy()

            mainapploop()
        else:
            error()
            

# making sure if the app is run for the first time
def checklooppin():
    print("Checking if the pin exists.")

    path_to_file = "pintest.scs"
    path = Path(path_to_file)
    if path.is_file():
        print("Pin found")
        mainloop2()

    else:
        print("Pin not found")
        mainloop1()
checklooppin()

# recovery code creation
def checklooprecovery():
    global firstrun
    global i


    path_to_file = 'test123.scs'
    path = Path(path_to_file)

    if path.is_file():
        print("Sucessfully found the file")
        
        firstrun = False
        if firstrun == False:
            print("firstrun = False")
            checklooppin()

    else:
        with open('test123.scs', 'w') as f:
            for i in range(4):
                value = randint(1000, 9999)
                value = str(value)

                f.write(value)
            print("created new file")
            f.close()
            checklooprecovery()
checklooprecovery()