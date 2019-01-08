# 爬虫入门
 - 参考资料
    - 《python网络数据采集》
    - 《精通Python爬虫框架Scrapy》
    - [Python3网络爬虫](https://blog.csdn.net/c406495762/article/details/72858983)
    - [Scrapy官方教程](https://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/tutorial.html)
 - 具备知识基础
    - url 
    - http协议
    - web前端,html、css、 js
    - ajax
    - re、xpath
    - xml
## 爬虫介绍
 - 爬虫定义：网络爬虫（又被称为网页蜘蛛，网络机器人，在FOAF社区中间，更经常的称为网页追逐者）， 
   是一种按照一定的规则，自动地抓取万维网信息的程序或者脚本。 另外一些不常使用的名字还有蚂蚁、自动索引、模拟程序或者蠕虫。
 - 两大特征
    - 能按作者要求下载数据或者内容
    - 能自动在网络上流窜
 - 三大步骤
    - 下载网页
    - 提取正确的信息
    - 根据一定规则自动跳到另外的网页上执行上两步内容
 - 爬虫分类
    - 通用爬虫
    - 专用爬虫（聚焦爬虫）
 - python网络包
    - Python2.x：urllib, urllib2, urllib3, httplib, httplib2, requests
    - Python3.x: urllib, urllib3, httplib2, requests
    - python2: urllib和urllib2配合使用，或者requests
    - Python3： urllib，requests
## urllib
 - 包含模块
    - urllib.request:打开和读取urls
    - urllib.error:包含urllib.request产生常见的错误，使用try捕获
    - urllib.parse:包含解析url的方法
    - urllib.robotparse：解析robots.txt文件
    - Example01
 - 网页编码问题的解决
    - charset可以自动检测页面文件的编码格式，但是，可能有误
    - 需要安装 conda install chardet
    - Example02
    
## urlopen
 - urlopen的返回对象
    - Example03
    - geturl:返回请求对象的url
    - info:请求反馈对象的meta信息
    - getcode:http请求code
    
## request.data:
 - 常用的访问网络的方法
    - post
    - get
    - Example04
 
     
    