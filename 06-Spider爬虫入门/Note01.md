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
    - get
        - 利用参数给服务器传递信息
        - 参数为dict，然后用parse编码
    - Example04
    
    - post
        - 一般向服务器传递参数使用
        - post是把信息自动加密处理
        - 如果想使用post信息，需要用到data参数
        - 使用post，意味着http的请求头可能需要更改：
            - Content-Type: application/json
            - Content-Length:数据长度
            - 简而言之，一旦更改请求方法，请注意请求头部信息相连接
        - urllib.parse.urlencode:可以将字符串自动换成上面的
    - Example05
    - 为了过多的设置请求信息，单纯的通过urlopen函数已经不能满足，需要使用request.Request类
    - Example06    
    
## urllib.error
 - URLError产生的原因
    - 网络未连接
    - 服务器连接失败
    - 找不到指定服务器
    - 是OSError的子类
    - Example07
 - HTTPError,是URLError的一个子类
    - Example08
 - 两者区别
    - HTTPError是对应的HTTP请求的返回码错误，如果返回设为错误码是400以上的，则引发HTTPError
    - URLError对应的一般是网络出现啊问题，包括url问题
    - 关系OSError-URLError-HTTPError
 - UserAgent
    - UserAgent:用户代理，简称UA，属于header的一部分，服务器通过UA来判断访问者身份
    - 常见的UA值，使用的时候可以直接复制粘贴，也可以用浏览器访问的时候抓包
    
            1.Android
            Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19
            Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30
            Mozilla/5.0 (Linux; U; Android 2.2; en-gb; GT-P1000 Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1

            2.Firefox
            Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0
            Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0

            3.Google Chrome

            Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36
            Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19

            4.iOS

            Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3
            Mozilla/5.0 (iPod; U; CPU like Mac OS X; en) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/3A101a Safari/419.3
    - 设置UA可以通过两种方式
        - heads
        - add_header
        - Example09
    - 
 
     
    