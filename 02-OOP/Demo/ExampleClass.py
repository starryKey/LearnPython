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

class A():
    pass

class B(A):
    pass

class C(B,A):
    pass

print(A.__mro__)
print(B.__mro__)
print(C.__mro__)


# 多继承
class Fish():
    def __init__(self,name):
        self.name = name
    def swim(self):
        print("I am swimming")

class Bird():
    def __init__(self,name):
        self.name = name
    def fly(self):
        print("I am flying")
class PersonD():
    def __init__(self,name):
        self.name = name
    def work(self):
        print("I am working")
class SuperMan(PersonD,Bird,Fish):
    def __init__(self,name):
        self.name = name

s = SuperMan("ChaoRen")
s.fly()
s.swim()
s.work()

#单继承

class Woker(PersonD):
        pass
woker = Woker("HH")
woker.work()


class PersonH():
    # name = ""
    # age = 18
    # 只能写一个构造函数❓❓❓
    # def __init__(self,name,age):
    #     self.name = name
    #     self.age = age
    #     print("name = {0}, age = {1}".format(name,age))
    def __init__(self):
        self.name = "Tom"
        self.age = 18
        print("name = {0}, age = {1}".format(self.name, self.age))
# ph = PersonH("Jack",18)
ph2 = PersonH()


class A():
    pass
class B(A):
    def __init__(self,name):
        print(name)
class C(B):
    #对父类构造函数进行扩展
    #第一种方式
    """
        def __init__(self,name,age):
        #首先调用父类的函数
        B.__init__(self,name)
        print(name)
        #其次增加自己的功能
        print(age)
    """

    #第二种方式，使用super调用
    def __init__(self,name):
        #首先调用父类构造函数
        super(C, self).__init__(name)
        #其次，再增加自己的功能
        print("C中的功能")




# cc = C("Tom",27)
ccc = C("Jane")


#Mixin写法

class PersonM():
    name = "Tom"
    age = 18
    def eat(self):
        print("Eat...")
    def drink(self):
        print("drink...")
    def sleep(self):
        print("sleep...")
class TeacherM(PersonM):
    def work(self):
        print("work...")
class StudentM(PersonM):
    def study(self):
        print("Study...")
class Tutor(TeacherM,StudentM):
    pass
t = Tutor()
print(Tutor.__mro__)
print(t.__dict__)
print(Tutor.__dict__)

#Mixin实现

class TeacherMixin():
    def work(self):
        print("work...")
class StudentMixin():
    def study(self):
        print("study")
class TutorM(PersonM, TeacherMixin, StudentMixin):
    pass

tt = TutorM()
print(TutorM.__mro__)
print(tt.__dict__)
print(TutorM.__dict__)

print(dir(TeacherMixin))

class PersonK():
    # fget、fset、fdel函数名可任意
    def fget(self):
        return self._name * 2

    def fset(self, name):
        self._name = name.upper()

    def fdel(self):
        self._name = "NoName"

    name = property(fget, fset, fdel, "测试")
    #对象后加()触发执行
    def __call__(self, *args, **kwargs):
        print("__call__")
    def __str__(self):
        return "TestStr(%s)"% self.name
    # def __repr__(self):
    #     return "TestRepr(%s)"% self.name
per1 = PersonK()
per1.name = "Jack"
print(per1.name)
print(PersonK.__dict__)
print(PersonK.__doc__)
print(PersonK.__name__)
print(PersonK.__bases__)
print(PersonK.__mro__)
# 对象当函数使用时，调用__call__方法

per1()

print(per1)
print(per1.__str__())
print(per1.__repr__())


class PersonM():
    name = "John"
    age = 18
    def __getattr__(self, item):
        print("没找到呀")
    def __setattr__(self, key, value):
        print("设置属性 key = {0}, value = {1}".format(key,value))
        #下面语句会造成死循环
        # self.key = key
        #为了避免死循环,给父类设置
        super().__setattr__(key, value)
        # super.__setattr__(self,key,value)
        #使用> <等比较符号时会触发
    def __gt__(self, other):
        return  self.name > other.name

perM = PersonM()

print(perM.name)
print(perM.log)

perM.sub = "iOS"
print(PersonM.__dict__)

class Manager():
    def __init__(self,name):
        self.name = name
    def __gt__(self, other):
        return  self.name < other.name


m1 = Manager("Jack")
m2 = Manager("Tom")
print(m1 > m2)

# 类和对象的三种方法
class PersonF():
    # 实例方法
    def eat(self):
        print(self)
        print("I am eating....")

    # 类方法
    # 类方法的第一个参数，一般命名为cls，区别于self
    @classmethod
    def play(cls):
        print(cls)
        print("I am playing....")
    #静态方法
    # 不需要使用第一个参数表示自身或类
    @staticmethod
    def say():
        print("Saying....")

personf = PersonF()
#实例方法
personf.eat()
#类方法
personf.play()
PersonF.play()
#静态方法
PersonF.say()
personf.say()

# 属性的三种操作用法
# 1、赋值
# 2、读取
# 3、删除
class StudentA():
    def __init__(self,name):
        self.name = name
        self.age = 18
a = StudentA("Tomy")
#读取
print(a.name)
print(a.age)
#赋值
a.age = 24
print(a.age)
# 删除
# del a.age
print(a.age)

# 类属性 property
# 应用场景
# 对变量除了普通的三种操作，还想增加一些附加的操作，则可通过property完成
class A():
    def __init__(self):
        self.name = "Tom"
        self.age = 20
    #模拟读取操作
    def fget(self):
        print("我被读取了")
        return self.name
    #模拟写入操作
    def fset(self, name):
        print("我被写入了")
        self.name = name + "测试写入"
    #模拟删除操作
    def fdel(self):
        pass
    # property的四个参数顺序是固定的
    # 第一个参数代表读取的时候调用
    # 第二个参数代表写入的时候调用
    # 第三个参数是删除
    # 第四个doc
    name2 = property(fget, fset, fdel, "这是一个property")
a = A()
print(a.name)
print(a.name2)
a.name2 = "Jack"
# print(a.name2)

#抽象
class AnimalA():
    #通常是子类继承，重写对应的的方法等；或者说父类不实现方法，子类实现对应的方法
    def sayHello(self):
        pass


# 抽象类的实现
import abc
#声明一个类并且指定当前类的元类

class Human(metaclass=abc.ABCMeta):

    # 定义一个抽象的方法
    @abc.abstractmethod
    def smoking(self):
        pass

    # 定义类抽象方法
    @classmethod
    def drink(cls):
        pass

    #定义静态类抽象方法
    @staticmethod
    def play():
        pass

    def sleeping(self):
        print("Sleeping......")

# 自定义类,类可以自己组装

class B():
    pass

# 任意定义一个函数
def say(self):
    print("Saying......")

say(9)
#函数名可以当变量用
B.say = say
b = B()
b.say()

# 自己组装类，示例

from types import MethodType
class Mo():
    pass
#任意定义一个函数
def sayHaha(self):
    print("Say haha .....")

mo = Mo()
mo.sayHaha = MethodType(sayHaha, Mo)
mo.sayHaha()


# help(MethodType)
#对象类型
# help(type)

# 利用type造一个类
# 先定义类应该具有的成员函数

def sayHi(self):
    print("sayHi....")
def talk(self):
    print("talking")

#用type来创建一个类
# (cls, what, bases=None, dict=None):
TestA = type("AName", (object,), {"class_say":sayHi,"class_talk":talk})

aa = TestA()
print(aa.__dict__)
help(TestA)

help(aa)
dir(aa)
#
aa.class_say()
aa.class_talk()


# 元类
# 元类写法是固定的，它必须继承自type

class TestMetaClass(type):
    # 注意以下写法
    def __new__(cls, *args, **kwargs):
        #自己的业务处理
        print("这是元类")
        return type.__new__(cls, *args, **kwargs)

# 定义玩就可以直接用了,注意写法
class TeacherHH(object, metaclass=TestMetaClass):
    pass
tthh = TeacherHH()
tthh.__dict__
