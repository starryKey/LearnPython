from tkinter import *


baseFrame = Tk()
baseFrame.title = "菜单"
baseFrame.geometry("400x300+300+100")

menubar = Menu(baseFrame)


emenu = Menu(baseFrame)
for item in ['Copy', 'Past', 'Cut']:
    emenu.add_command(label=item)

subemenu1 = Menu(baseFrame)
for item in ["New", "Save as"]:
    subemenu1.add_command(label=item)

subemenu2 = Menu(baseFrame)
for item in ["Delete"]:
    subemenu2.add_command(label=item)


menubar.add_cascade(label='File', menu=subemenu1)
menubar.add_cascade(label='Edit', menu=emenu)
menubar.add_cascade(label='About', menu=subemenu2)

baseFrame['menu'] = menubar

baseFrame.mainloop()