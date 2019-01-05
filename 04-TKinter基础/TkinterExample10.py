import tkinter

baseFrame = tkinter.Tk()

def btnClick(event):
        global  w
        w.move(id_ball, 12,5)
        w.move("fall", 0,5)



w = tkinter.Canvas(baseFrame, width=500, height=400)
w.pack()
w.bind("<Button-1>", btnClick)

# 创建组件后返回id
id_ball  = w.create_oval(20,20, 50,50, fill="green")

# 创建组件使用tag属性
w.create_text(123,56, fill="red", text="ILovePython", tag="fall")
# 创建的时候如果没有指定tag可以利用addtag_withtag添加
# 同类函数还有 addtag_all, addtag_above, addtag_xxx等等
id_rectangle = w.create_rectangle(56,78,173,110, fill="gray")
w.addtag_withtag("fall", id_rectangle)


baseFrame.mainloop()