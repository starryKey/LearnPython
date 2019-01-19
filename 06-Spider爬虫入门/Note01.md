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
            Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5

    - 设置UA可以通过两种方式
        - heads
        - add_header
        - Example09
    - ProxyHandler处理(代理服务器)
        - 使用代理IP，是爬虫的常用手段
        - 获取代理服务器的地址
            - www.xicidaili.com
            - www,goubanjia.com
        - 代理用来隐藏真是访问中，代理也不允许频繁访问某个固定网络，代理一定要很多个
    - 基本使用步骤
        - 1、设置代理地址
        - 2、创建ProxyHandler
        - 3、创建Opener
        - 4、安装Opener
    - Example10
 - cookie & session
    - 由于http协议的无记忆性，人们为了弥补这个缺陷，所采用的一个补充协议
    - cookie是发送给用户(访问者，如浏览器)的一段信息，session是保存在服务器上的对应的另一半信息，用来记录用户信息
 - cookie和session的区别
    - 存放位置不同
    - cookie不安全，cookie用户保存，session服务器保存
    - session会保存在服务器上一定时间，会过期
    - 单个cookie保存数据不超过4k,很多浏览器限制一个站点最多保存20个
 - session的存放位置
    - 存在服务器
    - 一般情况下，session是放在内存中或数据库中
    - 没有cookie登录Example11,根据结果可知，没使用cookie则返回网页为未登录        
 -  使用cookie登录
    - 直接把cookie复制下来，然后手动放入请求头中，Example12
    - http模块包含一些关于cookie的模块，通过他们则可自动使用cookie
        - CookieJar
            - 管理存储cookie，向传出的http请求添加cookie，
            - cookie存储在内存中，CookieJar实例回收后cookie将消失
        - FileCookieJar
            - 使用文件管理cookie
            - filename是保存cookie的文件
        - MozillaCookieJar
            - 创建与mocilla浏览器cookie.txt兼容的FileCookieJar实例
        - LwpCookieJar
            - 创建与libwww-perl标准兼容的Set-Cookie3格式的FileCookieJar实例
            
        - 关系：CookieJar-> FileCookieJar->MozillaCookieJar & LwpCookieJar
    - 利用CookieJar访问微博
        - 自动使用cookie登录，大致流程是
        - 打开登录页面后自动通过用户名密码登录
        - 自动提取反馈回来的cookie
        - 利用提取的cookie登录隐私页面
        - Example13，Mark：验证没绕过去。。。
    - handler是Handler的实例，常用的如下
        - 用来处理复杂请求
        
               #生成cookie的管理器
               cookie_handle = request.HTTPCookieProcessor(cookie)
               #创建http请求的管理器
               http_handle = request.HTTPHandler()
               #创建HTTPS管理器
               context = ssl._create_unverified_context()
               https_handle = request.HTTPSHandler(context=context)
    - 创建handler后，使用opener打开，打开后相应的业务有相应的handler处理
        - Example14,cookie作为一个变量，打印出来
        - cookie的属性
            - name: 名称
            - value:值
            - domain:可以访问此cookie的域名
            - path:可以访问此cookie的页面路径
            - expires:过期时间
            - size：大小
            - http字段
        - cookie的保存-FileCookieJar,Example15
        - cookie的读取
            - Example16
            
- SSL
 - SSL证书就是指遵守SSL安全套接层协议的服务器数字证书(SercureSocketLayer)    
 - 美国网景公司开发
 - CA(CertifacateAuthority)是数字证书认证中心，是发放、管理、废除数字证书的受信任的第三方机构
    - SSL(Secure Sockets Layer 安全套接层),及其继任者传输层安全（Transport Layer Security，TLS）是为网络通信提供安全及数据完整性的一种安全协议。TLS与SSL在传输层对网络连接进行加密
    - 遇到不信任的SSL证书，需要单独处理
    - Example17-ssl 
    
- js加密
 - 有的反爬虫策略采用js对需要传输的数据进行加密处理(通常取MD5值)
 - 经过加密，传输的就是密文，但是加密函数或者过程一定是在浏览器完成， 也就是一定会把代码(js代码)暴露给使用者
 - 通过阅读加密算法，就可以模拟出加密过程，从而达到破解
 - Example18,Example19解密
 
- ajax
 - 异步请求
 - 一定会有URL，请求方法，可能有数据
 - 一般使用格式
 - Example20
## Request 让HTTP服务人类
 - 更简洁更友好
 - 继承了urllib的所有特征
 - 底层使用的是urllib3
 - 开源地址：https://github.com/requests/requests
 - 中文文档：http://docs.python-requests.org/zh_CN/latest/index.html
 - 安装：conda install requests
 - get请求
    - requests.get(url)
    - requests.request("get",url)
    - 可以带有headers和parmas参数
    - 案例Example21
 - get返回内容
    - Example22 
 - post 
    - rsp = requests.post(url, data=data)
    - Example23
    - date, headers要求dict类型
 - proxy
    
       
 
 

      
            
            
                    
            
      
                
        
          
 
    
    
 
     
    