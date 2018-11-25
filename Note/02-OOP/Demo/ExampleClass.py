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

print(PythonStudent.__dict__)
print(jack.__dict__)

# 此时PythonStudent称为类实例
print("*" * 20)
print(id(PythonStudent.name))
print(id(PythonStudent.age))

# id可以鉴别一个变量是否和另一个变量相同
stu = PythonStudent()
print(id(stu.name))
print(id(stu.age))

stu.name = "Tom"
stu.age = "18"
print("*" * 20)
print(id(stu.name))
print(id(stu.age))

class Teacher():
    name = "Tom"
    subject = "English"

    # 非绑定类的方法 //相当于OC swift中 实例方法
    def teach(self):
        self.name = "Jane"
        self.subject = "math"
        print("name = {0},subject = {1}".format(self.name, self
                                                .subject))
    def teach2(s):
        print("name = {0},subject = {1}".format(s.name, s.subject))
    #类名绑定 //相当于OC swift中 类方法
    def teach3():
        print("name = {0},subject = {1}".format(__class__.name, __class__.subject))
    #构造函数
    def __init__(self):
        self.name = "John"
        self.subject = "History"
    def teach4(self):
        print("name = {0},subject = {1}".format(self.name, self
                                                .subject))

class BStudent():
    name = "xiaohua"
    subject = "English"

teacher1 = Teacher()
# teacher1.teach()
teacher1.teach2()
Teacher.teach3()

s = Teacher()
s.teach4()

#此时self被s替换
Teacher.teach4(s)
#同样可以把Teacher作为参数传进去
Teacher.teach4(Teacher)
#静态编译会进行强类型检查Java等
#此时，传入的是类实例B，因为BStudent具有name和subject属性，所以不会报错

Teacher.teach4(BStudent)
#以上代码，利用了鸭子模型

###私有属性的访问

class Person():
    name = "Jamas"
    __age = 18

a = Person()
a.name = "Tom"
# print(Person.__class__.name)
# age 检测不到

#私有成员变量，其实是可以访问的
print(a.__dict__)
print(Person.__dict__)

a._Person__age = 20
print(a._Person__age)


#继承的语法

class Engneer(Person):
    subject = "iOS"
    __ages = "28"
    __test = "hh"
    def playGame(self):
        print("玩游戏")

eng = Engneer()
eng.name = "Tom"
eng.playGame()
print(eng._Engneer__test)

print(eng.__dict__)
print(Engneer.__dict__)

print(eng._Engneer__ages)




print("**********************我是分割线***********************")

#构造函数
class Animal():
    pass
class Panda(Animal):
    # def __init__(self):
    #     print("我是国宝🐼")
    def __init__(self, name):
        print("我是{0}".format(name))
class Dog(Panda):
    def __init__(self):
        print("I am a dog")
class Cat(Panda):
    pass
# 实例化的时候，自动调用了Dog的构造函数，因为找到了构造函数，则停止向上查找

dog = Dog()
# 由于Cat没有构造函数，故向上查找，因为父类的构造函数需要两个参数，因此
cat = Cat("我是猫科动物")

print(type(super))
help(super)

