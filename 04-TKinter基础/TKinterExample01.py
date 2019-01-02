import tkinter
# 测试tkinter是否好用
# tkinter._test()

'''

Example1

base = tkinter.Tk()
#消息循环
base.mainloop()

'''

'''
Example2 Label

base = tkinter.Tk()
# 标题
base.wm_title("This is a label")
lb = tkinter.Label(base, text="Python Label")
# 给相应的组件指定布局
lb.pack()

base.mainloop()
'''

# 设置Label

'''

base = tkinter.Tk()
base.wm_title("Test Label")
#支持的属性很多,background,font,underline等
#第一个参数，指定所属
lbl = tkinter.Label(base, text="Python AI")
lbl.pack()

lbl2 = tkinter.Label(base, text="绿色", background="green")
lbl2.pack()

lbl3 = tkinter.Label(base, text="橘色", background="orange")
lbl3.pack()

base.mainloop()

'''


#Button

def showLbl():
    global baseFrame
    # 在函数中定义了一个label
    # label的父组件是baseFrame
    lb = tkinter.Label(baseFrame, text="显示Label")
    lb.pack()

baseFrame = tkinter.Tk()
#生成一个按钮，command参数指示，当按钮被按下的时候，执行哪个函数
btn = tkinter.Button(baseFrame, text="Show Label", command=showLbl)
btn.pack()

baseFrame.mainloop()

'''
Button的属性：

anchor 				设置按钮中文字的对其方式，相对于按钮的中心位置
background(bg) 		设置按钮的背景颜色
foreground(fg)		设置按钮的前景色（文字的颜色）
borderwidth(bd)		设置按钮边框宽度
cursor				设置鼠标在按钮上的样式
command				设定按钮点击时触发的函数
bitmap				设置按钮上显示的位图
font				设置按钮上文本的字体
width				设置按钮的宽度  (字符个数)
height				设置按钮的高度  (字符个数)
state				设置按钮的状态
text				设置按钮上的文字
image				设置按钮上的图片

'''













