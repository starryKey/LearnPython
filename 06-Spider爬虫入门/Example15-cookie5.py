


from urllib import request, error,parse
from http import cookiejar
import ssl



#创建cookiejar的实例
filename = "cookie.txt"
cookie = cookiejar.MozillaCookieJar(filename)

#生成cookie的管理器
cookie_handle = request.HTTPCookieProcessor(cookie)
#创建http请求的管理器
http_handle = request.HTTPHandler()
#创建HTTPS管理器
context = ssl._create_unverified_context()
https_handle = request.HTTPSHandler(context=context)

#创建请求管理器
opener = request.build_opener(http_handle, https_handle, cookie_handle)

def login():

    '''
    负责初次登录
    需要用户名密码，用来获取cookie凭证
    :return:
    '''
    #此URL需要从登录的form的action属性中提取
    # url = "https://weibo.com/login.php?url=https%3A%2F%2Fweibo.com%2Fu%2F3811132737%2Fhome%3Fwvr%3D5"
    url = "https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.19)"
    #微博要验证。。。

    data = {
        "username":"1056838379@qq.com",
        "password":"ljl547067"
    }

    context = ssl._create_unverified_context()

    #数据进行编码
    data = parse.urlencode(data)
    #创建一个请求
    req = request.Request(url, data=data.encode())
    #使用opener发起请求

    rsp = opener.open(req)

    # 保存cookie文件
    #ignore_discard表示即时cookie将要被丢弃也要保存下来
    #ignore_expires表示如果该文件中的cookie即使已经过期，保存
    cookie.save(ignore_discard=True, ignore_expires=True)

    # rsp = request.urlopen(req, context=context)

if __name__ == '__main__':
    '''
    执行完login后，会得到授权之后的cookie
    将cookie打印
    '''
    login()

    print(cookie)
    for item in cookie:
        print(type(item))
        print(item)
        for i in dir(item):
            print(i)




