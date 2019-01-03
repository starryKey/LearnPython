#pack布局案例
import tkinter

baseFrame = tkinter.Tk()
# 以下所有代码都是创建一个组件，然后布局

btn1 = tkinter.Button(baseFrame, text='A')
btn1.pack(side=tkinter.LEFT, expand=tkinter.YES, fill=tkinter.Y)

btn2 = tkinter.Button(baseFrame, text='B')
btn2.pack(side=tkinter.TOP, expand=tkinter.YES, fill=tkinter.BOTH)

btn2 = tkinter.Button(baseFrame, text='C')
btn2.pack(side=tkinter.RIGHT, expand=tkinter.YES, fill=tkinter.NONE,
          anchor=tkinter.NE)

btn2 = tkinter.Button(baseFrame, text='D')
btn2.pack(side=tkinter.LEFT, expand=tkinter.NO, fill=tkinter.Y)

btn2 = tkinter.Button(baseFrame, text='E')
btn2.pack(side=tkinter.TOP, expand=tkinter.NO, fill=tkinter.BOTH)

btn2 = tkinter.Button(baseFrame, text='F')
btn2.pack(side=tkinter.BOTTOM, expand=tkinter.YES)

btn2 = tkinter.Button(baseFrame, text='G')
btn2.pack(anchor=tkinter.SE)

baseFrame.mainloop()