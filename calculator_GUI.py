#follow vyom.coder on instagram for more projects

from tkinter import * #to install tkinter in your computer use pip install tk
import tkinter.messagebox as msg
import random


root = Tk()
root.geometry("410x450")
root.config(background="#2B2B2B")
root.title("Backchodi Calculator!!")

def abt():
    msg.showinfo(title= "About Calculator", message="Ayooo there are a billons of calculators out there but I am glad that u choose this (^_^), Bad Luck.")
    msg.showwarning(title="WARNING", message="Beaware, if you are offended you can climb up the himalayas and chill ;)")
def virus():
    msg.showwarning(title="VIRUS", message="Oh No humans do what they are said not too :)")
    msg.showwarning(title="VIRUS", message="Virus has been injected to your system (^o^)")
    msg.showwarning(title="VIRUS", message="Its was a prank >_< look at the camera behind you")
    msg.showwarning(title="VIRUS", message="joking there are no cameras you are safe (^o^)")
def ext():
    msg.showinfo(title="WHY??", message="Do you want to quit so soon (╥﹏╥)...\nsee you again byee")
    root.destroy()

my_menu = Menu(root, bg="#737373", fg="#ffffff", font="lucida 10 bold", activeforeground="#2B2B2B", activebackground="#737373")
my_menu.add_command(label="About Calci ;)", command=abt)
my_menu.add_command(label="DON'T CLICK", command=virus)
my_menu.add_command(label="Exit", command=ext)

root.config(menu= my_menu)


def calc(event):
    try:
        global entvarible
        global value
        text = event.widget.cget("text")
        print(text)
        if text == "=":
            value = eval(entvarible.get())
            entvarible.set(value)
            ent.update()

        elif text == "C":
            entvarible.set("")
            ent.update()
        else:
            entvarible.set(entvarible.get()+text)
            ent.update()
    except:
        a = ["Looks like someone missed the math class","Do You need a Calculator to Calculate your IQ too ;)?",  "You definitly gonna dissapoint your math teacher", "If math were a game,\nyou'd be the NPC that everyone ignores",]
        fun = random.randint(0, 4)
        msg.showerror(title="NOOB", message=f"{a[fun]}")
entvarible = StringVar()
entvarible.set("")


ent = Entry(root, textvariable=entvarible, font= "Roboto 25", background="#37474F", foreground="#FFFF00", justify=RIGHT)
ent.pack(fill=X, padx= 10, pady= 10, ipadx= 1, ipady= 1)


btnframe = Frame(root, relief= "solid", bg="#2B2B2B")
btnframe.pack()
btnframe1 = Frame(root, relief= "solid", bg="#2B2B2B")
btnframe1.pack()
btnframe2 = Frame(root, relief= "solid", bg="#2B2B2B")
btnframe2.pack()
btnframe3 = Frame(root, relief= "solid", bg="#2B2B2B")
btnframe3.pack()



btnlist1 = ["1", "2", "3", "="]
for i in btnlist1:
    btn = Button(btnframe, text= i, width=4, height=2, bg="#FFAB40", activebackground="#FFFFFF", highlightbackground="#FFD180", font="Roboto  15", foreground="#FFFFFF", activeforeground="#000000")
    btn.pack(side=LEFT, padx= 15, pady= 15)
    btn.bind('<Button-1>', calc)


btnlist2 = ["4", "5", "6", "+"]
for j in btnlist2:
    btn1 = Button(btnframe1, text= j, width=4, height=2, bg="#FFAB40", activebackground="#FFFFFF", highlightbackground="#FFD180", font="Roboto  15", foreground="#FFFFFF", activeforeground="#000000")
    btn1.pack(side=LEFT, padx= 15, pady= 15)
    btn1.bind('<Button-1>', calc)


btnlist3 = ["7", "8", "9", "-"]
for k in btnlist3:
    btn2 = Button(btnframe2, text= k, width=4, height=2, bg="#FFAB40", activebackground="#FFFFFF", highlightbackground="#FFD180", font="Roboto  15", foreground="#FFFFFF", activeforeground="#000000")
    btn2.pack(side=LEFT, padx= 15, pady= 15)
    btn2.bind('<Button-1>', calc)


btnlist4 = [".", "0", "C", "/"]
for l in btnlist4:
    btn3 = Button(btnframe3, text= l, width=4, height=2, bg="#FFAB40", activebackground="#FFFFFF", highlightbackground="#FFD180", font="Roboto  15", foreground="#FFFFFF", activeforeground="#000000")
    btn3.pack(side=LEFT, padx= 15, pady= 15)
    btn3.bind('<Button-1>', calc)



root.mainloop()
