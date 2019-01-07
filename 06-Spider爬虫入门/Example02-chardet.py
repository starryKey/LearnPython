'''
使用urllib.request请求一个网页，并将内容打印出来

'''

from urllib import request
import chardet

if __name__ == '__main__':
    url = "http://www.tulingxueyuan.com"
    # 打开对应的URL并把相应页面作为返回
    rsp = request.urlopen(url, data=None, timeout=5)

    #把返回结果读取出来，读取出来的内容为bytes
    rspData = rsp.read()

    # 将bytes转为字符串需要解码
    # result = rspData.decode()
    # print(result)

    # 使用chardet自动检测
    cs = chardet.detect(rspData)
    print(type(cs))
    # cs 为dict,使用get取，能取到就使用，否则为utf-8
    rspData = rspData.decode(cs.get("encoding", "utf-8"))
    print(rspData)