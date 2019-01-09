'''
利用parse模块模拟post请求
分析步骤：
1、使用检查浏览器
2、尝试输入单词girl，发现每输入一个字母后都有请求
3、请求地址为：https://fanyi.baidu.com/sug
4、利用Network-->All-Headers查看，发现formData的值是kw:girl
5、检查返回内容格式，发现返回的是json格式内容，需要使用json包

'''

from urllib import request, parse
import ssl
import json


'''
主要流程
1、利用data构造内容，然后urlopen打开
2、返回一个json格式
3、结果就应该是搜索关键字对应的释义　

'''
baseurl = "http://fanyi.baidu.com/sug?"
keyword = input("Please input your keyword:")
#存放用来模拟form的数据，一定是dict格式
data = {
    'kw':keyword
    #该写法为硬编码
    #'kw':"girl"
}
#需要使用parse模块对data进行编码
enData = parse.urlencode(data).encode("utf-8")
print(type(enData))

# 需要一个请求头，请求头部至少包含传入的数据的长度
# request要求传入的请求头是一个dict格式

headers = {
    #因为是post请求，至少应该包含 content-length字段
    'Content-Length':len(enData)
}

# 有了Headers,data,url，就可以请求了

context = ssl._create_unverified_context()

# req = request.Request(url=baseurl, data=enData, headers=headers)
# rsp = request.urlopen(req, context=context)

rsp = request.urlopen(baseurl, data=enData, context=context)

json_data = rsp.read().decode("utf-8")
print(type(json_data))
print(json_data)

for item in json_data["data"]:
    print(item["k"], "--", item["v"])

