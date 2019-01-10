'''
URLError的使用
'''

from urllib import request, error
import ssl

if __name__ == '__main__':
    url = "https://www.baidu.com/test/hhh"
    url = "http://www.sipo.gov.cn/www"
    try:
        context = ssl._create_unverified_context()
        req = request.Request(url=url)
        resp = request.urlopen(req, context=context)
        html = resp.read().decode()
        print(html)
    except error.HTTPError as httperror:
        print("HTTPError {0}".format(httperror))
    except error.URLError as err:
        print("URLError {0}".format(err.reason))
    except Exception as e:
        print(e)