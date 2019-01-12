'''
使用代理访问百度

'''
import ssl
from urllib import request, error

if __name__ == '__main__':

    url = "http://www.baidu.com"

    # 1、设置代理地址
    proxy = {"http":"223.82.247.121:80"}
    # 2、创建ProxyHandler
    proxy_handler = request.ProxyHandler(proxy)
    # 3、创建Opener
    opener = request.build_opener(proxy_handler)
    # 4、安装Opener
    request.install_opener(opener)

    # 使用代理服务器访问

    try:
        context = ssl._create_unverified_context()
        rsp = request.urlopen(url,context=context)
        html = rsp.read().decode()
        print(html)
    except error.URLError as err:
        print(err)
