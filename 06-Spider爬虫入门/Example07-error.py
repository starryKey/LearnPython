'''
URLError的使用
'''

from urllib import request, error

if __name__ == '__main__':
    url = "https://www.baidu.com"
    try:
        req = request.Request(url=url)
        resp = request.urlopen(req)
        html = resp.read().decode()
        print(html)
    except error.URLError as err:
        print("URLError {0}".format(err.reason))
    except Exception as e:
        print(e)