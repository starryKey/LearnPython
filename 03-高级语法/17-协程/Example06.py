import threading
# 导入异步IO包
import asyncio

#使用协程
# @asyncio.coroutine
# 用async 替换 asyncio.coroutine
async def hello():
    print("Hello world (%s)" % threading.currentThread())
    print("Start....(%s)" % threading.currentThread())
    # await asyncio.sleep(3)  await 替换 yield from
    yield from asyncio.sleep(3)

    print("Done....(%s)" % threading.currentThread())
    print("Hello again (%s)" % threading.currentThread())

# 启动消息循环
# loop = asyncio.get_event_loop()
# # 定义任务
# tasks = [hello(), hello()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

# 写文件和网络都是IO操作

@asyncio.coroutine
def wget(host):
    print("wget %s....." % host)
    #异步请求网络地址
    connect = asyncio.open_connection(host, 80)
    # 注意yield from 的用法
    reader, writer = yield from connect
    header = "GET / HTTP/1.0\r\nHost:%s\r\n\r\n" % host
    writer.write(header.encode("utf-8"))

    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        # http协议的换行
        if line == b"\r\n":
            break
        print("%s header > %s" % (host, line.decode("utf-8").rstrip()))
    writer.close()

loop2 = asyncio.get_event_loop()

tasks2 = [wget(host) for host in ["www.baidu.com", "www.sina.com.cn", "www.sohu.com"]]
loop2.run_until_complete(asyncio.wait(tasks2))

loop2.close()





