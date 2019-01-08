'''
使用urllib.request请求一个网页，并将内容打印出来
对URL参数进行编码的方法需要使用parse模块
'''

from urllib import request, parse

if __name__ == '__main__':
    url = "http://www.baidu.com/s?"
    # 打开对应的URL并把相应页面作为返回

    keyword = input("Input your keyword:")
    # 要想使用data，需要使用字典结构
    qs = {
        "wd":keyword
    }
    par = parse.urlencode(qs)
    print("par={0}".format(par))

    fullurl = url + par
    print(fullurl)
    #直接使用wd="大熊猫"会出错
    rsp = request.urlopen(fullurl)

    # 把返回结果读取出来，读取出来的内容为bytes
    html = rsp.read()
    # 将bytes转为字符串需要解码
    result = html.decode()

    print(type(rsp))
    print(rsp)

    # print("URL:{0}".format(rsp.geturl()))
    # print("Info:{0}".format(rsp.info()))
    # print("code:{0}".format(rsp.getcode()))
    print(result)