import tkinter
from tkinter import *
import random
from tkinter import messagebox

answers = [
    "python",
    "java",
    "swift",
    "canada",
    "india",
    "america",
    "london",
]

words = [
    "nptoyh",
    "avja",
    "wfsit",
    "cdanaa",
    "aidin",
    "aiearcm",
    "odnlon",
]

num = random.randrange(0,7,1)


def res():
    global words,answers,num
    num = random.randrange(0,7,1)
    lbl.config(text=words[num])
    e1.delete(0, END)

def default():
    global words,answers,num
    lbl.config(text = words[num])


def checkans():
    global words,answers,num
    var = e1.get()
    if var == answers[num]:
        messagebox.showinfo("Success","This is a correct answer")
        res()
    else:
        messagebox.showerror("Error","This is not correct answer")
        e1.delete(0, END)


    
root = tkinter.Tk()
root.geometry("350x400+400+300")
root.title("Jumbbled")
root.configure(background="#000000")

lbl = Label(
    root,
    text = 'Your here',
    font = ("Verdana", 18),
    bg = "#000000",
    fg = "#ffffff",
)
lbl.pack(pady=30,ipady=10,ipadx=10)


ans1 = StringVar()
e1 = Entry(
    root,
    font = ("Verdana", 16),
    textvariable = ans1
)
e1.pack(ipady=5,ipadx=5)

btncheck = Button(
    root,
    text = 'check',
    font = ("Comic sans ms", 16),
    width = 16,
    bg = "#4C4B4B",
    fg = "#6ab04c",
    relief = GROOVE,
    command = checkans
)
btncheck.pack(pady=40)

btnreset = Button(
    root,
    text = 'reset',
    font = ("Comic sans ms", 16),
    width = 16,
    bg = "#4C4B4B",
    fg = "#EA425C",
    relief = GROOVE,
    command = res
)
btnreset.pack()


default()
root.mainloop()
