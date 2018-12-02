# 常用模块
 - calendar
 - time
 - datetime
 - timeit
 - os
 - shutil
 - zip
 - matn
 - string
        
           上述所有的模块使用理论上应该先导入，string除外
           calendar, time, datetime的区别参考中文意思
           
## calendar
 - 日历

##
 - 时间戳
    - 一个时间表示，根据不同语言，可以是整数或者浮点数
    - 是从1970年1月1日0时0分0秒到现在经历的秒数
    
 - UTC时间   
    - UTC又称为世界协调时间， 以英国的格林尼治天文所在区域的时间做世界标准时间
    - 中国的时间为 UTC+8 东八区
    
## 夏令时
 - 夏令时就是在夏天的是时间将时间调快一小时，每天变成25小时，本质没变还是24小时

## 时间元组
 - 一个包含时间内容的普通元组
 
                
   索引      内容    属性            值

    0       年       tm_year     2015
    1       月       tm_mon      1～12
    2       日       tm_mday     1～31
    3       时       tm_hour     0～23
    4       分       tm_min      0～59
    5       秒       tm_sec      0～61  60表示闰秒  61保留值
    6       周几     tm_wday     0～6
    7       第几天    tm_yday     1～366
    8       夏令时    tm_isdst    0，1，-1（表示夏令时）
     