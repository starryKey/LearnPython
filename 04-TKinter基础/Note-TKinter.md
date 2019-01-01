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