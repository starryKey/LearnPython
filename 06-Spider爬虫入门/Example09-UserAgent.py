'''
访问一个网站
更改自己的UserAgent进行伪装

'''

from urllib import request, error
import ssl

if __name__ == '__main__':

    url = "https://www.baidu.com"

    try:
        #使用head方法伪装
        # headers = {}
        # headers["User-Agent"] = "Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3"
        # req = request.Request(url, headers=headers)

        #使用add_header方法
        req = request.Request(url)
        req.add_header("User-Agent", "Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3")


        context = ssl._create_unverified_context()

        rsp = request.urlopen(req, context=context)
        html = rsp.read().decode()

        print(html)

    except error.HTTPError as err:
        print(error)
    except error.URLError as err:
        print(err)
    except Exception as err:
        print(err)