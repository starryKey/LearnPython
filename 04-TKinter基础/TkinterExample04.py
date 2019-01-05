# 普通菜单的代码
import tkinter

baseFrame = tkinter.Tk()

menubar = tkinter.Menu(baseFrame)

for item in ['File', 'Edit', 'View', 'About']:
    menubar.add_command(label=item)

baseFrame['menu'] = menubar

baseFrame.mainloop()