#导入P01
#模块不能以数字开头
#可借助importlib包实现导入以数字开头的模块名称
"""
import importlib
# 导入"01"模块
test = importlib.import_module("01")

"""

import P01

#导入的时候起别名
# import P01 as PyModule
stu = P01.Student("Jamas",24)
stu.say()

P01.sayHello()

