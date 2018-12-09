
# 案例01
# 打开文件，用写的方式
# f称为文件句柄
# r表示后面字符串内容不需要转义
# f = open(r"Test01.txt", "w")
# 打开后需关闭
# f.close()
# 上述示例说明：以写方式打开文件，默认是如果没有文件，则创建

#案例02
# with 语句
# with 语句使用的技术是一种称为上下文管理协议的技术(ContextManagerProtocol)
# 自动判断文件的作用域， 自动关闭不再使用的打开的文件句柄
with open(r"test01.txt",'r') as fi:
    pass
    # 下面语句块开始对文件f进行操作
    # 在本模块中不需要再使用close文件关闭文件f

with open(r"Test01.txt","r") as f:
    #按行读取内容
    strline = f.readline()
    #此结构保证能够完整读取文件直到结束
    while strline:
        print(strline)
        strline = f.readline()

print(f)

# read是按字符读取文件内容
# 允许输入参数决定读取几个字符，如果没指定，从当前位置读取到末尾
# 否则，从当前位置读取指定个数字符
with open(r"Test01.txt", "r") as f:
    strChar = f.read(6)
    print(strChar)
    print(len(strChar))


# list 能用打开的文件作为参数，把文件内每一行内容作为一个元素

with open(r"Test01.txt","r") as f:
    l = list(f)
    for i in l:
        print(i)


# seek (offset, from)
#  - 移动文件的读取位置，也叫读取指针
#  - from的取值范围：0：从文件头开始偏移，1：从文件当前位置开始偏移；2：从文件末尾开始偏移
# 移动的单位是字节
# 一个汉字是由若干个字节构成的
# 返回文件只针对当前位置。

# seek 案例
# 打开文件后，从第五个字节开始读取

with open(r"test01.txt", "r") as f:
    #seek开始移动字节,一个汉字三个字节，故两个汉字从6开始
    f.seek(6, 0)
    strChar = f.read()
    print(strChar)

# 练习
# 打开文件，三个字符一组读出内容，然后显示在屏幕上
# 每读一次，休息一秒钟
#
print("***" * 10)
import time
# with open(r"test01.txt", "r") as f:
#     # read 参数的单位是字符，可以理解成一个汉字就是一个字符
#     strChar = f.read(3)
#     while strChar:
#         print(strChar)
#         # sleep参数为秒
#         time.sleep(1)
#         strChar = f.read(3)

# tell函数：用来显示文件读写指针的当前位置
# with open(r"test01.txt", "r") as f:
#     strChar = f.read(3)
#     pos = f.tell()
#
#     while strChar:
#         print(pos)
#         print(strChar)
#
#         strChar = f.read(3)
#         pos = f.tell()
# 以上结果说明：
# tell的返回数字的单位是byte
# read是以字符为单位

# write：文件的写操作
# write(str): 把字符串写入文件
# writeline(str): 把字符串按行写入文件,表示写入很多行
# 区别：1、write函数参数只能是字符串；2、writeline的参数可以是字符串，也可以是字符序列

# 示例

# with open(r"Test01.txt",'a') as f:
    #注意字符串内含有换行符
    # f.write("\n 生活不止眼前的苟且, \n 还有诗和远方的田野")
# 也可以直接写入行

with open(r"Test01.txt",'a') as f:
    #注意字符串内含有换行符
    # f.write("\n 生活不止眼前的苟且, \n 还有诗和远方的田野")
    f.writelines("生活不止眼前的苟且 \n")
    f.writelines("还有诗和远方的田野")

list1 = ["Test", "hello", "world"]
# a代表追加方式打开
with open(r"Test01.txt",'w') as f:
    f.writelines(list1)


# 持久化 - pickle
#  - 序列化(持久化,落地)：把程序运行中的信息保存在磁盘上
#  - 反序列化：序列化的逆过程
#  - pickle： python提供的序列化模块
#  - pickle.dump:序列化
#  - pick.load：反序列化

import pickle

# 序列化
# age = 18
# with open(r"Test01.txt", "wb") as f:
#     pickle.dump(age,f)


# 反序列化

# with open(r"Test01.txt", "rb") as f:
#     age = pickle.load(f)
#     print(age)

#
with open(r"Test02.txt","w") as f:
    pass

# 示例
# 序列化:可以保存一些结构化的东西
# a = [24,"Jack","I love playing basketball",[172,65]]
# with open(r"test02.txt", "wb") as f:
#     pickle.dump(a, f)
# 反序列化

# with open(r"test02.txt", "rb") as f:
#     aTest = pickle.load(f)
#     print(aTest)

print("***" * 10)
# 使用shelve创建文件并使用
import shelve

# 示例
# 打开文件
# shelve相当于一个字典
shv = shelve.open(r"shv.db")

shv["one"] = 1
shv["two"] = 2
shv["three"] = 3

shv.close()

#  通过以上案例发现，shelve自动创建的不仅仅是一个"shv.db"文件，还包括其他格式文件
# tips：Mac下子看到了shv.db文件。。。。Windows不一样

# shelve 读取案例
shv2 = shelve.open(r"shv.db")

try:
    print(shv2["one"])
    print(shv2["two"])
    # print(shv2["four"])
except Exception as err:
    print("出错了:{0}".format(err))
finally:
    shv2.close()

import os
print(os.getcwd())

# shelve 特性
#1、不支持多个应用并行写入：为了解决这个问题，open的时候可以使用flag=r
#2、写会问题：（1）、shelve恶魔人情况下不会等待持久化对象进行任何修改；2、解决方法，强制写回：writeback=True

# shelve 只读方式打开

shv3 = shelve.open("/Users/wol/Desktop/Study/LearnPython/03-高级语法/14-文件File/shv.db", flag="r")
try:
    k1 = shv3["one"]
    print(k1)
finally:
    shv3.close()

# 案例

shv4 = shelve.open(r"shv.db")
try:
    shv4["one"] = {"Str1":1, "Str2":2, "Str3":3}
finally:
    shv4.close()
shv5 = shelve.open(r"shv.db")
try:
    one = shv5["one"]
    print(one)
finally:
    shv5.close()

print("***" * 10)
# 常见错误：shelve忘记写回，需要使用强制写回

# shv6 = shelve.open(r"shv.db")
# step 02 强制写回
shv6 = shelve.open(r"shv.db", writeback=True)
try:
    k1 = shv6["one"]
    print(k1)
    # 修改k1["Str1"]的值，但是这只是还在内存中，实质并没有修改db; step01
    # 此时一旦shelve关闭，
    k1["Str1"] = 1000
finally:
    shv6.close()

shv7 = shelve.open(r"shv.db")
try:
    k1 = shv7["one"]
    print(k1)
    # 修改k1["Str1"]的值，但是这只是还在内存中，实质并没有修改db
finally:
    shv7.close()

# shelve 使用with管理上下文环境

with shelve.open(r"shv.db", writeback=True) as shvA:
    k1 = shvA["one"]
    print(k1)
    #此时一旦shelve关闭，则内容还是存在于内存中，没有写回数据库
    k1["Str1"] = 10000

with shelve.open(r"shv.db") as shvB:
    print(shvB["one"])
