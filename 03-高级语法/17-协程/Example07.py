# aiohttp 案例

# import asyncio
# from aiohttp import web

import time
from concurrent.futures import ThreadPoolExecutor

def return_future(msg):
    time.sleep(3)
    return msg
# 创建一个线程池

pool = ThreadPoolExecutor(max_workers=2)

# 往线程池中加入2个task

f1 = pool.submit(return_future, "Test")
f2 = pool.submit(return_future, "Test2")

#
print(f1.done())
time.sleep(3)
print(f2.done())

print(f1.result())
print(f2.result())

