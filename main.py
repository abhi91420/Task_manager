from time import strftime, time
from tkinter import *


class Gui:

    # constructor
    def __init__(self, root):
        self.root = root
        self.root.title("TASKS")
        self.root.geometry("300x700")
        self.root.resizable(width=False, height=False)
        self.clock = Label(self.root, fg="blue")
        self.clock.grid(row = 0,column = 0,padx = 80,pady = 40)
        self.update_clock()
        self.new_button = Button(self.root, text="New",command = self.newwindow).grid(row = 0, column =1)
        self.r =0
    # clock
    def update_clock(self):
        now = strftime("%H:%M:%S")
        self.clock.configure(text=now)
        self.clock.after(1000, self.update_clock)

    # label creator
    def label(self, txt):
        self.l = Label(self.root, text=txt, fg="red",pady =15)
        self.l.grid(row = self.r, column =0)

    # button creator
    def donebutton(self):
        self.b = Button(self.root, text="Done")
        self.b.grid(row = self.r,column = 1)

    # create a task
    def task(self,txt):
        self.r +=1
        self.label(txt)
        self.donebutton()

    # display gui method
    def display(self):
        self.root.mainloop()

    # new window
    def newwindow(self):
        self.newwindow = Toplevel(self.root)
        self.newwindow.title("NEW TASK")
        self.newwindow.geometry("300x200")
        self.newwindow.resizable(width=False, height=False)
        Label(self.newwindow,text="Task").grid()
        self.t1 = Text(self.newwindow,height = 2,width = 36)
        self.t2 = Text(self.newwindow,height = 2,width = 10)
        self.t1.grid()
        Label(self.newwindow, text="Time").grid()
        self.t2.grid()
        self.c_b=Button(self.newwindow,text = "CREATE")
        self.c_b.grid()

if __name__ == '__main__':
    a = Gui(Tk())
    a.display()
