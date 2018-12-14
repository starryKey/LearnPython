
import threading
import time

# 参数定义最多几个线程同时使用资源
semaphore = threading.Semaphore(3)

def func():
    if semaphore.acquire():
        for i in range(5):
            print(threading.current_thread().getName() + 'get semaphore' + " ")
        time.sleep(15)
        semaphore.release()
        print(threading.current_thread().getName() + 'release semaphore' + " ")

for i in range(8):
    t1 = threading.Thread(target=func)
    t1.start()
