"""
定义一个学生类

"""
class Student():
    # 一个空类，pass代表直接跳过
    # 此处pass必须有
    pass

# 定义一个对象
tom = Student()

# 再定义一个类，用来描述学Python的学生

class PythonStudent():
    #使用None给不确定的值赋值
    #name = None
    name = ""
    age = 20
    course = "Python"
    # 需要注意
    # 1、def doHomeWork  的缩进层级
    # 2、系统默认有一个self参数
    def doHomeWork(self):
        print(" {0} 在做作业".format(self.name))

        # 函数末尾建议使用None语句
        return None


jack = PythonStudent()
jack.name = "Jack"
jack.age = 24
jack.doHomeWork()


