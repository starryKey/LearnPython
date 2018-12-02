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
# 返回值:字符传 Tue Jun 6 11:11:00 2017
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

det1 = time.time()
p()
print(time.time()-det1)

cDemo = '''
sum = []
for i in range(1000):
    sum.append(i)
'''

# 示例02
# 利用timeit 调用代码，执行10000次，查看运行时间
det2 = timeit.timeit(stmt="[i for i in range(1000)]", number=10000)
# 测试代码C执行10000次运行结果
det3 = timeit.timeit(stmt=cDemo, number=10000)

print(det2)
print(det3)

# timeit 可以执行一个函数，来测量一个函数的执行时间

def doIt():
    num = 3
    for i in range(num):
        print(i)

det4 = timeit.timeit(stmt=doIt, number=10)
print(det4)

sDemo = '''
def doIt(num):
    for i in range(num):
        print(i)
'''
#执行doIt(num):
#setup负责把环境变量准备好

det5 = timeit.timeit("doIt(num)", setup=sDemo+"num=3", number=10)
print(det5)
