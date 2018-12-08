
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
with open(r"test01.txt", "r") as f:
    # read 参数的单位是字符，可以理解成一个汉字就是一个字符
    strChar = f.read(3)
    while strChar:
        print(strChar)
        # sleep参数为秒
        time.sleep(1)
        strChar = f.read(3)






