# 01 lambda表达式
#一个参数

stm = lambda x:100 * x
res1 = stm(10)
print(res1)
# 多个参数
stm2 = lambda x,y,z:x + y * 10 + z * 100
res2 = stm2(2,3,4)
print(res2)

print("*" * 15 +  "我是分割符" + "*" * 15)

# 02 高阶函数

# 变量可以赋值
a = 100
b = a
# 函数名称就是一个变量
def funcA():
    print("I am funcA")
funcA()
print(funcA)
funcB = funcA
print(funcB)
# 以上代码结论：
#1、函数名称是变量
#2、funcA和funcB只是名称不一样而已
#3、既然函数名称是变量，则应该可以被当作参数传入另一个函数

# 高阶函数举例
# funcA是普通函数，返回一个传入数字的100倍数字

def funcC(n):
    return n * 100
#再写一个函数，把传入参数乘以300
def funcD(n):
    return funcC(n) * 300
print(funcC(10))
print(funcD(10))

#写一个高阶函数
def funE(n,f):
    #假定函数是把扩大100倍
    return f(n) * 3
print(funE(3, funcC))



# 系统高阶函数- 01 - map
# 原意就是映射，即把集合或列表的元素，每一个元素都按照一定的规则进行操作，生成一个新的列表或集合
# map函数是系统提供的具有映射功能的函数，返回值是一个迭代对象
# 关于map python 2.x 返回列表， 3.x返回迭代器

# 示例：对列表中的每一个元素乘以10，并得到新的列表
# 方法1 遍历
list1 = [1,2,3,4,5,6]
list2 = []
for i in list1:
    list2.append(i * 10)

print(list1)
print(list2)

# 方法2 map实现

def mulTen(n):
    return n * 10

list3 = map(mulTen, list1)
print(list3)
# map 类型是一个可迭代的结构， 所以可以使用for遍历
for i in list3:
    print(i)

def square(x):
    return x ** 2
rst2 = map(square,[1,2,3])
for i in rst2:
    print(i)

print(rst2)

rst3 = map(lambda x,y:x + y,[1,3,5,7,9],[2,4,6,8,10])
for i in rst3:
    print(i)

print(rst3)

# 系统高阶函数- 02 - reduce
# 原意是归并，缩减
# 把一个可迭代对象最后归并成一个结果
# 对于作为参数的函数要求：必须由两个参数，必须有返回结果
# reduce 需要导入functools包
# reduce([1,2,3,4,5]) == f(f(f(f(1,2),3),4),5)

# 导入
from functools import reduce
# 定义一个操作函数
# 加入操作函数只能相加

def testAdd(x,y):
    return x + y
# 对于列表[1,2,3,4,5]执行testAdd的reduce操作
rst = reduce(testAdd, list1)
print(type(rst))
print(rst)

# 系统高阶函数- 02 - filter
# 过滤函数：对一组数据进行过滤，符合条件的数会生成一个新的队列并返回
# 跟map相比较
# - 相同：都是对列表的每一个元素逐一进行操作
#     - 不同：
#         - map会生成一个跟原来数据相对应的新队列
#         - filter不一定，只有符合条件的才会进入新的队列
#     - filter怎么写：
#         - 利用给定函数进行判断
#         - 返回值一定是个bool值
#         - 格式调用:filter(f,data),f是过滤函数，data是数据


# 示例：过滤偶数成为一个新列表
# 需要定义过滤函数
# 过滤函数要求有输入，返回bool值
def isEven(a):
    return a % 2 == 0
list4 = [1,2,3,4,23,4.5,6.8,7.9,80,25,42,16]
list5 = filter(isEven, list4)
print(type(list5))
# 返回的filter内容是一个可迭代的对象
print(list5)
print(id(list5))
# print([i for i in list5])
# 转为list
list6 = list(list5)
print(list6)
print(list5)
print(id(list5))
# mark:为什么执行过一次迭代后，再迭代时没有值？
for i in list5:
    print(i)

print("*" * 15 +  "我是分割符" + "*" * 15)


### 高阶函数 - 排序
 # - 把一个序列按照给定算法进行排序
 # - key：在排序前对每一个元素进行key函数运算，可以理解成按照key函数定义的逻辑进行排序
 # - python 2.x 和python 3.x相差很大

# 示例1
listA = [1,11,21,31,20,10,6,30]
listB = sorted(listA, reverse=True)
print(listB)
# 示例2
listC = [-10,2,10,6,-16,80,-8]
# 按照绝对值进行排序
listD = sorted(listC, key=abs, reverse=True)
print(listD)
help(sorted)

# sorted案例

aStr = ["haha","Hello","World","test","tomorrow"]
aStr2 = sorted(aStr)
print(aStr2)

aStr3 = sorted(aStr, key=str.lower)
print(aStr3)

### --- 返回函数
# - 函数可以返回一个具体的值，也可以返回一个函数作为结果

# 普通函数
def myFunc(a):
    print("My  func")
    return None
a = myFunc(8)
print(a)

# 返回函数, 函数作为返回值返回， 被返回的函数在函数体内定义

def myFunc2():

    def myFunc3():
        print("Func 3")
        return 3
    return myFunc3

myFunc4 = myFunc2()
print(type(myFunc4))
print(myFunc4)
myFunc4()


# 复杂的返回函数例子
# args 参数列表
def myFunc5( *args):
    def myFunc6():
        rest1 = 0
        for n in  args:
            rest1 += n
        return rest1
    return myFunc6

myfunc7 = myFunc5(1,2,3,4,5,6,7,8,9,0)
print(myfunc7())
myfunc7()

func8 = myFunc5(10,20,30,40)
print(func8())

### --- 闭包
# - 当一个函数在内部定义函数，并且内部的函数应用外部函数的参数或者局部变量，当内部函数被当作返回值的时候，
# - 相关参数和变量保存在返回值的函数中，这种结果，叫闭包
# myFunc5 函数即为标准闭包结构

#常见坑
def count():
    #定义列表
    fs = []
    for i in range(1,4):
        def fu():
            return i * i
        fs.append(fu)

    return fs
f1,f2,f3 = count()
print(f1())
print(f2())
print(f3())
# 出现的问题，返回函数引用了变量i，i并非立即执行，而是等到三个函数都返回的时候才统一使用，此时i已经变成了3，最终调用的时候，结果均为3 * 3
# 注意问题： 返回闭包时，返回函数不能引用任何循环变量
# 解决方案：再创建一个函数，该函数绑定循环变量的当前值，无论该循环变量以后如何改变，已经绑定的函数参数值不再改变

# 修改上述函数

def count2():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i))
    return fs
f4,f5,f6 = count2()
print(f4())
print(f5())
print(f6())

