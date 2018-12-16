# 案例01
list1 = [i for i in range(6)]
# list1是可迭代的，但不是迭代器
for index in list1:
    print(index)
# range是个迭代器
for ind in range(3):
    print(ind)

# isinstance案例
# 判断某个变量是否是一个实例

# 判断是否可迭代

from collections import Iterable

# 是可迭代的
list2 = [1,2,3,4,5]
print(isinstance(list2, Iterable))

# from collections import Iterator

from collections import Iterator

# 但不是迭代器
print(isinstance(list2, Iterator))

#iter 函数

s = "Hello world"
print(isinstance(s, Iterable))
print(isinstance(s, Iterator))
# 将可迭代的对象转为迭代器
s_iter = iter(s)

print(isinstance(s_iter, Iterable))
print(isinstance(s_iter, Iterator))


# 生成器

#直接使用生成器
list3 = [x * x for x in range(5)]# 放在中括号中是列表生成器
list4 = (x * x for x in range(5))# 放在小括号中就是生成器

print(type(list3))
print(type(list4))

# 函数案例

def Test1():
    print("Step 1")
    print("Step 2")
    print("Step 3")
    return None

Test1()

print("***" * 20)

# 生成器案例
# 在Test2函数中，yield用于返回

def Test2():
    print("Step 1")

    yield "ts"
    print("Step 2")
    yield "hh"
    print("Step 3")
    yield "ll"

g = Test2()
ger = next(g)
print(ger)

print(next(g))
print(next(g))


# for循环调用生成器

#普通写法
def fib(max):
    n,a,b = 0, 0, 1
    while n < max:
        print(b)
        a,b = b, a + b
        n += 1

    return "Done"

print(fib(5))


# 生成器写法
def fib(max):
    n,a,b = 0, 0, 1
    while n < max:
        #print(b)
        yield b
        a,b = b, a + b
        n += 1

    return "Done"

gg = fib(5)

for i in range(6):
    rst = next(gg)
    print(rst)
