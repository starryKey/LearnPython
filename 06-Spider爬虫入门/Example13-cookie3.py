


from urllib import request, error,parse
from http import cookiejar
import ssl


#创建cookiejar的实例

cookie = cookiejar.CookieJar()
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
        "password":""
    }

    context = ssl._create_unverified_context()

    #数据进行编码
    data = parse.urlencode(data)
    #创建一个请求
    req = request.Request(url, data=data.encode())
    #使用opener发起请求

    rsp = opener.open(req)
    # rsp = request.urlopen(req, context=context)

def getHomePage():

    # url = "https://weibo.com/login.php?url=https%3A%2F%2Fweibo.com%2Fu%2F3811132737%2Fhome%3Fwvr%3D5"
    url = "https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.19)"
    #如果已经执行了login函数，则opener自动已经包含了相应的cookie


    try:
        # context = ssl._create_unverified_context()
        rsp = opener.open(url)

        # req = request.Request(url)

        # rsp = request.urlopen(req, context=context)

        html = rsp.read().decode()
        with open("rsp3.html", "w") as f:
            f.write(html)

    except error.URLError as err:
        print(err)
    except error.HTTPError as err:
        print(err)


if __name__ == '__main__':
    login()
    getHomePage()

