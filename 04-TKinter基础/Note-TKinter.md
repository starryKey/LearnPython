# GUI介绍
 - GraphicalUserInterface,
 - GUI for Python: Tkinter, wxPython, PyQt
 - TKinter:
    - 绑定的是TK GUI工具集，用途Python包装的Tcl代码
 - PyGTK
    - Tkinter的替代品
 - wxPython
    - 跨平台的Python GUI
 - PyQt
    - 跨平台的
    - 商业授权可能由问题
 - 推荐资料
    - 辛星GUI， 辛星Python
    - Python GUI Programming cookbook
    - Tkinter reference a GUI for Python
    
## Tkinter 常用组件
 - 按钮
  
        Button                按钮组件
        RadioButton            单选框组件
        CheckButton            选择按钮组件
        Listbox                列表框组件
 - 文本输入组件
        
        Entry                单行文本框组件
        Text                多行文本框组件
 - 标签组件
        
        Label                标签组件，可以显示图片和文字
        Message                标签组件，可以根据内容将文字换行
 - 菜单
        
        Menu                菜单组件
        MenuButton            菜单按钮组件，可以使用Menu代替
 - 滚动条
        
        scale                滑块组件
        Scrollbar            滚动条组件
 - 其他组件
        
        Canvas                画布组件
        Frame                框架组件，将多个组件编组
        Toplevel            创建子窗口容器组件
 - 组件的大致使用步骤
        
        创建总面板
        创建面板上的各种组件
        指定组件的父组件，即依附关系
        利用相应的属性对组件进行设置
        给组件安排布局
        同步骤2相似，创建好多个组件
        最后，启动总面板的消息循环
        
## 组件布局
 - 控制组件的摆放方式
 - 三种布局：
    - pack: 按照方位布局
    - place: 按照坐标布局
    - grid： 网格布局
 - pack布局
    - 最简单，代码量最少，挨个摆放，默认从上倒下，系统自动设置
    - 通用使用方式为： 组件对象.pack(设置，，，，，，，）
    - side: 停靠方位， 可选值为LEFT,TOP,RIGHT,BOTTON
    - fill: 填充方式,X,Y,BOTH,NONE
    - expande: YES/NO
    - anchor: N,E,S,W,CENTER
    - ipadx: x方向的内边距
    - ipady: y
    - padx: x方向外边界
    - pady： y........
 - grid布局
    - 通用使用方式：组件对象.grid(设置,,,,,,,)
    - 利用row，column编号，都是从0开始
    - sticky： N,E,S,W表示上下左右，用来决定组件从哪个方向开始
    - 支持ipadx，padx等参数，跟pack函数含义一样
    - 支持rowspan，columnspan，表示跨行，跨列数量
 - place布局
    - 明确方位的摆放
    - 相对位置布局，随意改变窗口大小会导致混乱
    - 使用place函数，分为绝对布局和相对布局，绝对布局使用x，y参数
    - 相对布局使用relx，rely, relheight, relwidth
    
## 消息机制
 - 消息的传递机制
    - 自动发出事件/消息
    - 消息由系统负责发送到队列
    - 由相关组件进行绑定/设置
    - 后端自动选择感兴趣的事件并作出相应反应
 - 消息格式
    - <[modifier-]---type-[-detail]>
    - <Button-1>: Button表示一个按钮事件，1代表的是鼠标左键，2代表中键
    - <KeyPress-A>:键盘A键位
    - <Control-Shift-KeyPress-A>:同时按下Control，Shift，A三个键
    - <F1>:F1键盘
    - [键位对应名称](https://infohost.nmt.edu/tcc/help/pubs/tkinter/web/key-names.html )
    - 示例TkinterExample02
## Tkinter的绑定
 - bind_all：全局范围的绑定，默认的是全局快捷键，比如F1是帮助文档
 - bind_class: 接受三个参数，第一个是类名，第二个是事件，第三个是操作
     - w.bind_class("Entry", "<Control-V>", test_paste)
 - bind：单独对某个实例绑定
 - unbind：解绑，需要一个参数，即要解绑哪个事件
     
## Entry
 - 输入框，功能单一
 - entry["show"] = "*",设置遮挡字符
 - 案例：TkinterExample03
 
## 菜单

### 普通菜单
 - 第一个Menu类定义的是parent
 - add_command 添加菜单项，如果菜单是顶层菜单，则从左向右添加，否则就是下拉菜单
 - label： 指定菜单项名称
 - command: 点击后相应的调用函数
 - acceletor： 快捷键
 - underline： 制定是否菜单信息下有横线
 - menu：属性制定使用哪一个作为顶级菜单
 - TkinterExample04
### 级联菜单
 - add_cascade:级联菜单，作用是引出后面的菜单
 - add_cascade的menu属性：指明把菜单级联到哪个菜单上
 - label： 名称
 - 过程：
    - 1、建立menu实例
    - 2、add_command
    - 3、add_cascade
    - TkinterExample05
### 弹出式菜单
 - 也叫上下文菜单
 - 实现的大致思路
    - 1、建立菜单并向菜单添加各种功能
    - 2、监听鼠标右键
    - 3、如果右键点击，则根据位置判断弹出
    - 4、调用Menu的pop方法
 - add_separator:添加分隔符
 - Example07
 
### canvas画布
 - 画布： 可以自由的在上面绘制图形的一个小舞台
 - 在画布上绘制对象， 通常用create_xxxx，xxxx=对象类型， 例如line，rectangle
 - 画布的作用是把一定组件画到画布上显示出来
 - 画布所支持的组件：
    - arc
    - bitmap
    - image(BitmapImage, PhotoImage)
    - line
    - oval
    - polygon
    - rectangle
    - text
    - winodw（组件）
 - 每次调用create_xxx都会返回一个创建的组件的ID，同时也可以用tag属性指定其标签
 - 通过调用canvas.move实现一个一次性动作
 - Example08
 