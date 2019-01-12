

from urllib import request, error
import ssl

if __name__ == '__main__':
    url = "https://weibo.com/login.php?url=https%3A%2F%2Fweibo.com%2Fu%2F3811132737%2Fhome%3Fwvr%3D5"

    try:

        context = ssl._create_unverified_context()

        rsp = request.urlopen(url, context=context)

        html = rsp.read().decode()
    except error.URLError as err:
        print(err)
    except error.HTTPError as err:
        print(err)


    with open("rsp.html", "w") as f:
        f.write(html)

