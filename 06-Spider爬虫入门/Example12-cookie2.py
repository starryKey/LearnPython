

import ssl
from urllib import request, error

if __name__ == '__main__':

    url = "https://weibo.com/login.php?url=https%3A%2F%2Fweibo.com%2Fu%2F3811132737%2Fhome%3Fwvr%3D5"

    headers = {
        "Cookie":"YF-V5-G0=8d4d030c65d0ecae1543b50b93b47f0c; login_sid_t=993ee629be0b309615663d9f9df4be5a; cross_origin_proto=SSL; Ugrow-G0=9642b0b34b4c0d569ed7a372f8823a8e; WBStorage=24482d986ffad754|undefined; _s_tentry=passport.weibo.com; Apache=3207225965898.326.1547306826070; SINAGLOBAL=3207225965898.326.1547306826070; ULV=1547306826161:1:1:1:3207225965898.326.1547306826070:; WBtopGlobal_register_version=681ae76632252dfc; wb_view_log=1280*8002%261024*13662; SUB=_2A25xPngZDeRhGeVG6lMQ8yzLyDuIHXVSSu7RrDV8PUNbmtBeLUPakW9NT9bD95vl1N7csfZ_c7MG4uCeKjjNSUG_; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWfY3aokYz0.z03vNY6D7YS5JpX5KzhUgL.FoeReK2pe0zNe0M2dJLoIp-LxKBLBo.L1-qLxKnLB--LBoyNdc7t; SUHB=0YhBp9lcR30Ig3; ALF=1578843079; SSOLoginState=1547307081"
    }
    try:

        context = ssl._create_unverified_context()

        req = request.Request(url=url,headers=headers)

        rsp = request.urlopen(req,context=context)

        html = rsp.read().decode()
    except error.URLError as err:
        print(err)
    except error.HTTPError as err:
        print(err)

    with open("rsp2.html", "w") as f:
        f.write(html)