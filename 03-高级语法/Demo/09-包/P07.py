from pkg02 import *

stu = PP01.Student("John",20)
stu.say()

#定义了__all__ = ['PP01'] 故无论__init__中有其他什么，都不会被导入
# inInit()