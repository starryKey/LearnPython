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


