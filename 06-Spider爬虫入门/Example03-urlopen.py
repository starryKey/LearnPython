'''
使用urllib.request请求一个网页，并将内容打印出来

'''

from urllib import request

if __name__ == '__main__':
    url = "http://www.tulingxueyuan.com"
    # 打开对应的URL并把相应页面作为返回
    rsp = request.urlopen(url, data=None, timeout=5)

    print(type(rsp))
    print(rsp)
    print("URL:{0}".format(rsp.geturl()))
    print("Info:{0}".format(rsp.info()))
    print("code:{0}".format(rsp.getcode()))


    #把返回结果读取出来，读取出来的内容为bytes
    # rspData = rsp.read()

    # 将bytes转为字符串需要解码
    # result = rspData.decode()
    # print(result)