# 定义一个类
# 一个函数
#打印语句

class Student():
    def __init__(self, name="Tom", age=18):
        self.name = name
        self.age = age

    def say(self):
        print("My name is {0}, I am {1} years old".format(self.name, self.age))


def sayHello():
    print("Hello,I am Jack")
# 这句话的含义是只有在当前模块时调用，其他模块导入时，不执行
if __name__ == "__main__":
    print("这是模块P01")

