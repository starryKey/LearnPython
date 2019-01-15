from urllib import request
import ssl

url = "https://www.12306.cn/mormhweb"

context = ssl._create_unverified_context()

rsp = request.urlopen(url, context=context)

html = rsp.read().decode()
print(html)

