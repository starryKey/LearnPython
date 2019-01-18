'''
使用参数headers和params
研究返回结果

'''

import requests

#完整访问URL是下面URL加上参数构成
url = "http://www.baidu.com/s?"

kw = {
    "wd":"Test"
}

headers = {
    "User-Agent":"Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1"
}

rsp = requests.get(url, params=kw, headers=headers)
print(rsp.text)
print(rsp.content)
print(rsp.url)
print(rsp.encoding)
print(rsp.status_code)