from time import strftime, time
from tkinter import *


class Gui:

    # constructor
    def __init__(self, root):
        self.root = root
        self.root.title("TASKS")
        self.clock = Label(self.root,fg="blue")
        self.clock.pack(anchor='n')
        self.update_clock()

    # clock
    def update_clock(self):
        now = strftime("%H:%M:%S")
        self.clock.configure(text=now)
        self.clock.after(1000, self.update_clock)

    # label creator
    def label(self,txt):
        self.l = Label(self.root,text=txt)
        self.l.pack()
    # button creator
    def button(self, flag):
        tags = ["New", "Done"]
        self.b=Button(self.root, text=tags[flag])
        self.b.pack()

    # create a task
    def task(self, flag ,txt):
        self.label(txt)
        self.button(flag)

    # display gui method
    def display(self):
        self.root.mainloop()


if __name__ == '__main__':
    a = Gui(Tk())

    a.display()
