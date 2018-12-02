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