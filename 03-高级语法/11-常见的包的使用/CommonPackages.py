#常见的模块
# 01 日历
import calendar
"""
    calendar 获取一年的日历的字符串
    参数
        w = 每个日期之间的间隔字符数
        l = 每周占用的行数
        c = 每个月之间的间隔字符数
"""

cal1 = calendar.calendar(2018)
print(type(cal1))
# print(cal1)

cal2 = calendar.calendar(2018,l=2,c=5)
# print(cal2)

# isleap 判断某一年是否是闰年
isleap = calendar.isleap(2000)
print(isleap)
# leapdays: 获取指定年份之间的闰年的个数
nCount = calendar.leapdays(2001,2018)
print(nCount)
help(calendar.leapdays)

# month() 获取某个月的日历字符串
# 格式 calendar.month(年，月)
# 回值  月日历的字符串
cal3 = calendar.month(2018, 12)
print(cal3)

# 获取某年的某个月的天数
cal4 = calendar.monthlen(2018,12)

# monthrange()获取一个月的周几开始和天数
# 格式：calendar.monthrange(年,月)
# 返回值：元组（周几开始，总天数）
# 注意：周默认0～6，表示周一到周日

# help(calendar.monthrange(2018, 11))
w,t = calendar.monthrange(2018,11)
print(w)
print(t)

# monthcalendar() 返回一个月每天的矩阵列表
# 格式：calendar.monthcalendar(年，月)
# 返回值：二级列表
# 注意： 矩阵中没有天数用0表示

cal5 = calendar.monthcalendar(2018, 12)
print(cal5)

# prcal 直接打印日历
# calendar.prcal(2018)

# prmonth()直接打印整个月的日历
# 格式：calendar.prmonth(年，月)
# 返回值：无

calendar.prmonth(2018,11)

# weekday() 获取周几
# 格式：calendar.weekday(年，月， 日)
# 返回值， 周几对应的数字
weekday = calendar.weekday(2018,12,11)
print(weekday)



## 02 time模块

import time

#时间模块属性
# timezone: 当前时区和UTC时间相差的秒数，在没有夏令时的情况下
# altzone  获取当前时区与UTC时间相差的秒数，在有夏令时的情况下
# daylight 测当前是否是夏令时时间状态， 0 表示是

print(time.timezone)
print(time.altzone)
print(time.daylight)

# 得到时间戳
time.time()

# localtime 得到当前时间的时间结构
# 可以通过点号操作符得到相应的属性元素的内容

t = time.localtime()
print(t)
# print(t.tm_mday)

# asctime() 返回元组的正常字符串化之后的时间格式
# 格式 time.asctime(时间元组)
# 返回值:字符串 Tue Jun 6 11:11:00 2017
tl = time.localtime()
tt = time.asctime(tl)
help(time.asctime)

# ctime: 获取字符串化的当前时间
t3 = time.ctime()
print(t3)

# mktime() 使用时间元组获取对应的时间戳
# 格式：time.mktime(时间元组)
# 返回值：浮点数时间戳

t4 = time.mktime(time.localtime())
print(t4)

# clock: 获取CPU时间， 3.0~3.3版本直接使用， 3.6 调用有问题

# sleep 使程序进入睡眠， n秒后继续
for i in range(1,20):
    if i == 10:
        # time.sleep(5)
        print(i)


# t5 = time.clock()
# time.sleep(3)
# t6 = time.clock()
# print(t6 - t5)

# 按格式输出时间
# strftime：将时间元组转化为自定义的字符串格式

"""

格式  含义  备注
%a  本地（locale）简化星期名称    
%A  本地完整星期名称    
%b  本地简化月份名称    
%B  本地完整月份名称    
%c  本地相应的日期和时间表示    
%d  一个月中的第几天（01 - 31）   
%H  一天中的第几个小时（24 小时制，00 - 23）   
%I  一天中的第几个小时（12 小时制，01 - 12）   
%j  一年中的第几天（001 - 366）  
%m  月份（01 - 12） 
%M  分钟数（00 - 59）    
%p  本地 am 或者 pm 的相应符    注1
%S  秒（01 - 61）  注2
%U  一年中的星期数（00 - 53 星期天是一个星期的开始）第一个星期天之前的所有天数都放在第 0 周   注3
%w  一个星期中的第几天（0 - 6，0 是星期天） 注3
%W  和 %U 基本相同，不同的是 %W 以星期一为一个星期的开始  
%x  本地相应日期  
%X  本地相应时间  
%y  去掉世纪的年份（00 - 99）    
%Y  完整的年份   
%z  用 +HHMM 或 -HHMM 表示距离格林威治的时区偏移（H 代表十进制的小时数，M 代表十进制的分钟数）      
%%  %号本身

"""

formatter_ymdHMS = "%Y-%m-%d %H:%M:%S"
formatter_ymdHM = "%Y-%m-%d %H:%M"
formatter_ymd = "%Y-%m-%d"

# 返回样式 2018-12-02
# 传入样式 2018-12-02 22:36 或者 1543761337.12188或者1543761337
# time.localtime(timeRes) 获取float时间元组
# time.strptime(timeRes, formatter_ymdHMS),获取指定时间格式的时间元组
# time.strftime(formatter_ymdHMS, 时间元组) 时间元组转"指定格式"的字符串


def getdateStr_ymd(timeRes):
    try:
        if isinstance(timeRes, str):#传入的是str类型
            return  time.strftime(formatter_ymd, time.strptime(timeRes, formatter_ymdHMS))
        elif isinstance(timeRes, float): #传入的是float类型
            return time.strftime(formatter_ymd, time.localtime(timeRes))
        elif isinstance(timeRes, int):
            return time.strftime(formatter_ymd, time.localtime(float(timeRes)))
        else:
            return  timeRes
    except Exception as err:
        print(err)
        return timeRes




forTime = getdateStr_ymd("2018-12-02 22:36:16")
print(forTime)

t7 = time.localtime()
ft = time.strftime("%Y年%m月%d日 %H:%m", t7)
print(ft)


# 03 datetime 模块
# datetime提供日期和时间的运算和表示
# datetime 常见属性
# datetime.date: 一个理想的日期，提供year，month, day 属性

import datetime

dt1 = datetime.date(2018, 12, 2)
print(dt1)
print(dt1.year)
print(dt1.month)
print(dt1.day)

# datetime.time: 提供一个理想的时间，提供hour，minute,second, microsec的内容
# datetime.datetime: 提供日期和时间的组合
# datetime.timedelta: 提供一个时间差，时间长度

dt2 = datetime.time(23,16,36)
print("时{0}分{1}秒{2}".format(dt2.hour,dt2.minute, dt2.second))

# datetime.datetime

from datetime import datetime
# 常用类方法：
# today
# now
# utcnow
#fromtimestamp： 从时间戳中返回本地时间

dt3 = datetime(2018,12,2)
print(dt3.today())
print(dt3.now())

print(time.time())
print(dt3.fromtimestamp(time.time()))

# datetime.timedelta
# 表示一个时间间隔

from datetime import  datetime, timedelta

td1 = datetime.now()
td1.strftime("%Y-%m-%d %H:%M:%S")

print(td1)

td2 = timedelta(hours=1)
# 当前时间加上时间间隔后，把得到的一小时以后的时间格式化输出

print((td1+td2).strftime("%Y-%m-%d %H:%M:%S"))


# 04 timeit - 时间测量工具
import timeit

# 测量程序运行时间间隔实验

# 示例01
def p():
    time.sleep(1)

# det1 = time.time()
# p()
# print(time.time()-det1)

cDemo = '''
sum = []
for i in range(1000):
    sum.append(i)
'''

# 示例02
# 利用timeit 调用代码，执行10000次，查看运行时间
# det2 = timeit.timeit(stmt="[i for i in range(1000)]", number=10000)
# 测试代码C执行10000次运行结果
# det3 = timeit.timeit(stmt=cDemo, number=10000)

# print(det2)
# print(det3)

# timeit 可以执行一个函数，来测量一个函数的执行时间

def doIt():
    num = 3
    for i in range(num):
        print(i)

# det4 = timeit.timeit(stmt=doIt, number=10)
# print(det4)

sDemo = '''
def doIt(num):
    for i in range(num):
        print(i)
'''
#执行doIt(num):
#setup负责把环境变量准备好

# det5 = timeit.timeit("doIt(num)", setup=sDemo+"num=3", number=10)
# print(det5)


# 05 os模块

import os

#(一)
# getcwd 获取当前的工作目录
# 格式 os.getcwd()
# 返回值：当前工作目录的字符串
# 当前工作目录就是程序在进行文档相关操作，默认查找文件的目录

mydir = os.getcwd()
print(mydir)

# (二)
# chdir()改变当前的工作目录
# change directory
# 格式 os.chdir(路径)
# 返回值: 无

# os.chdir("/Users/wol/Desktop/Study/LearnPython/03-高级语法/")
# mydir2 = os.getcwd()
# print(mydir2)

# (三)
# listdir() 获取一个目录中所有的子目录和文件的名称列表
# 格式：os.listdir(路径)
# 返回值: 所有子目录和文件名称的列表

ld = os.listdir()
print(ld)

# (四)
# makedirs() 递归创建文件夹
# 格式：os.makedirs(路径)
# 返回值: 无
#  递归路径：多个文件夹夹层包含的路径就是递归路径，例如 "a/b/c/..."
# help(os.makedirs)


# (五)
# system() 运行系统shell命名
# 格式：os.system(系统命令)
# 返回值: 打开一个shell或者终端界面
# 一般推荐使用subprocess 代替

#例如
# os.system("ls")
# rst 返回结果为None
rst = os.system("cd")
# 在当前目录下创建一个dir的文件夹
# rst2 = os.system("touch dir")
# os.system("rm dir")

# (六)
# getenv() 获取指定的系统环境变量值
# 相应的有putenv()
# 格式：os.getenv("环境变量名")
# 返回值:  指定环境变量名对应的值

rst3 = os.getenv("PATH")
print(rst3)

# (七) exit 对出当前程序
# 格式：exit()
# 返回值：无

# 值部分
# - os.curdir:  当前目录
# - os.pardir:  父亲目录
# - os.sep: 当前系统的路径分隔符
# - os.linesep: 当前系统的换行符
# - os.name:  当前系统的名称

# tips:
# 在路径相关的操作中，不要手动拼写地址，因为手动拼写的路径可能不具有可移植性， 不同操作系统的操作符不同

print(os.name)

# 06 os.path 模块 跟路径相关的模块

import os.path as op

# 01 abspath() 将路径转化为绝对路径
# 格式： os.path.abspath("路径")
# 返回值: 路径的绝对路径形式


# linux 中
# . 号， 代表当前目录
# .. ，代表父目录
absp = op.abspath(".")
print(absp)

# 02 basename() 获取路径中的文件部分
# 格式： os.path.basename("路径")
# 返回值: 文件名字符串

bn = op.basename("/Users/wol/Desktop/Study/LearnPython")
print(bn)
bn = op.basename("/Users/wol/Desktop/Study/LearnPython/03-高级语法")
print(bn)

# 03 join（) 将多个路径拼合成一个路径
# 格式 os.path.join(路径1，路径2....)
# 返回值: 组合之后的新路径字符串

path1 = "Test/Local"
path2 = "haha.txt"

path3 = op.join(path1,path2)
print(path3)

# 04 split（) 将路径切割为文件夹部分和当前文件部分
# 格式 os.path.split(路径)
# 返回值: 路径和文件名组成的元组

t = op.split(path3)
print(t)

# 05 isdir() 检测是否是目录
# 格式os.path.isdir(路径)
# 返回值: 布尔值

rst4 = op.isdir("Test/Local/haha.txt")

# 06 exists() 检测文件或者目录是否存在
# 格式os.path.exists(路径)
# 返回值: 布尔值
rst5 = os.path.exists("Test/Local/haha.txt")
print(rst5)

# shutil模块

import shutil

# copy() 复制文件
# 格式：shutil.copy(来源路径，目标路径)
# 返回值：返回目标路径
# 拷贝的同时，可以给文件重命名

# rst6 = shutil.copy("Test/Local/haha.txt","Test/Local/lala.txt")
# print(rst6)

# copy2() 复制文件,保留元数据（文件信息）
# 格式：shutil.copy2(来源路径，目标路径)
# 返回值：返回目标路径
# 注意，copy和copy2的唯一区别在于copy2 在复制时保留元数据


# copyfile() 将一个文件中的内容复制到另外一个文档中
# 格式 shutil.copyfile("源路径"，"目标路径")
# 返回值： 无

# move() 移动文件/文件夹
# 格式 shutil.move("源路径"，"目标路径")
# 返回值：目标路径
# rst7 = shutil.move("local/path1/file.txt","/local/path2")

## 归档和压缩
# - 归档：把多个文件或者文件夹合并到一个文件当中
# - 压缩：用算法把多个文件或者文件夹无损或者有损合并到一个文件当中

# make_archive() 归档操作
# 格式: shutil.make_archive("归档之后的目录和文件名"，"后缀"，"需要归档的文件夹")
# 返回值：归档后的地址
local = os.curdir
print(local)
rst8 = shutil.make_archive("/Users/wol/Desktop/Study/LearnPython/03-高级语法/TestFile02","zip","/Users/wol/Desktop/Study/LearnPython/03-高级语法/11-常见的包的使用/TestFile")
print(rst8)
# help(shutil.make_archive)

# unpack_archive() 解包操作
# 格式: shutil.unpack_archive("归档文件地址"，"解包后的地址")
# 返回值：解包之后的地址

# zip 压缩包
# 压缩模块
import zipfile

# #zipfile.ZipFile(file[, mode[, compression[, allowZip64]]])
# # 创建一个ZipFile对象，表示一个zip文件。参数file表示文件的路径或类文件对象(file-like object)；
# 参数mode指示打开zip文件的模式，默认值为’r’，表示读已经存在的zip文件，也可以为’w’或’a’，’w’表示新建一个zip文档或覆盖一个已经存在的zip文档，
# ’a’表示将数据附加到一个现存的zip文档中。参数compression表示在写zip文档时使用的压缩方法，它的值可以是zipfile. ZIP_STORED 或zipfile. ZIP_DEFLATED。
# 如果要操作的zip文件大小超过2G，应该将allowZip64设置为True。
zf1 = zipfile.ZipFile("/Users/wol/Desktop/Study/LearnPython/03-高级语法/TestFile02.zip")
print(zf1)
# ZipFile.getinfo(name):
# 获取zip文档内指定文件的信息。返回一个zipfile.ZipFile对象，它包括文件的详细信息

zf2 = zf1.getinfo("001.txt")
print(zf2)

# ZipFile.namelist()
# 获取zip文档内所有文件的名称列表

nl = zf1.namelist()
print(nl)

# ZipFile.extractall([path[, members[, pwd]]])
# 解压zip文档中的所有文件到当前目录。参数members的默认值为zip文档内的所有文件名称列表，也可以自己设置，选择要解压的文件名称。

zfRst = zf1.extractall("/Users/wol/Desktop/Study/LearnPython/03-高级语法")
print(zfRst)

import random

# random模块
# random() 获取0-1之间的随机小数
# 格式random。random（）
# 返回值：随机0-1之间的小数

print(random.random())

# choice() 随机返回序列中的某个值
# 格式 random.choice(序列)
# 返回值 序列中的某个值

li = [str(i) + "Test" for i in range(10)]
print(li)
result1 = random.choice(li)
print(result1)

# shuffle() 随机打乱列表
# 格式：random.shuffle(列表)
# 返回值: 打乱顺序后的列表

li2 = [i for i in range(10)]
print(li2)
random.shuffle(li2)
print(li2)

# randint(a,b): 返回一个a到b之间的随机整数，包含a和b

print(random.randint(0,100))



