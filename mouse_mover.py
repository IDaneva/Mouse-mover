import random
import time
import pyautogui
from tkinter import *
from tkinter import ttk


class MyWindow:
    def __init__(self, win):
        self.seconds_entry_lbl = Entry(win, width=7)
        self.seconds_entry_lbl.grid(column=2, row=2, sticky=(W, E))
        self.move_button = Button(win, text="Move!", command=self.move_mouse).grid(column=3, row=3, sticky=W)
        self.text_label1 = Label(win, text="Move mouse for ").grid(column=1, row=2, sticky=E)
        self.text_label2 = Label(win, text="minutes").grid(column=3, row=2, sticky=W)

    def move_mouse(self):
        minutes = self.seconds_entry_lbl.get()
        x = random.randint(600, 700)
        y = random.randint(200, 600)
        pyautogui.moveTo(x, y, 0.5)
        #
        # t_end = time.time() + 60 * int(minutes)
        # while time.time() < t_end:
        #     pyautogui.moveTo(x, y, 0.5)


root = Tk()
mywin = MyWindow(root)
root.title('Mouse mover')
root.geometry("400x250+10+10")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

for child in mainframe.winfo_children():
    child.grid_configure(padx=10, pady=10)

root.mainloop()
# TODO: make a GUI
# TODO: make it possible to be ran outside the console

