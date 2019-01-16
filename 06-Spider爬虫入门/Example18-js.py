'''
破解有道词典
'''

from urllib import request, parse

def youdao(key):

    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

    data = {

        'i':'iOS',
        'from':'AUTO',
        'to':'AUTO',
        'smartresult':'dict',
        'client':'fanyideskweb',
        'salt':'15476510685276',
        'sign':'939d2f83db81d29296d819518a8997fa',
        'ts':'1547651068527',
        'bv':'8c1d961492d2126df817a1dafe4e9e56',
        'doctype':'json',
        'version':'2.1',
        'keyfrom':'fanyi.web',
        'action':'FY_BY_REALTIME',
        'typoResult':'false'
    }

    # 参数data需要的是bytes格式
    data = parse.urlencode(data).encode()

    headers = {
        'Accept': 'application/json,text/javascript,*/*;q=0.01',
        # 'Accept-Encoding': 'gzip,deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '257',
        'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8',
        'Cookie':'OUTFOX_SEARCH_USER_ID=-543350551@10.169.0.83;JSESSIONID=aaaHC_SNWE-Ggca55lxHw; OUTFOX_SEARCH_USER_ID_NCOO=865872399.0819657; ___rl__test__cookies=1547651068523',
        'Host':'fanyi.youdao.com',
        'Origin':'http://fanyi.youdao.com',
        'Referer':'http://fanyi.youdao.com/',
        'User-Agent':"Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1",
        'X-Requested-With':'XMLHttpRequest'

    }

    req = request.Request(url=url, data=data, headers=headers)
    rsp = request.urlopen(req)

    html = rsp.read().decode()
    print(html)

if __name__ == '__main__':
    youdao("iOS")