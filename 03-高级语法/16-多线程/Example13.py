import threading
import time

lock_1 = threading.Lock()
lock_2 = threading.Lock()


def func_1():
    print("func_1 starting......")
    lock_1.acquire()
    print("func_1 申请了lock_1...")
    time.sleep(2)
    print("func_1 等待lock_2...")
    lock_2.acquire()
    print("func_1 申请了lock_2...")

    lock_2.release()
    print("func_1 释放了lock_2...")

    lock_1.release()
    print("func_1 释放了lock_1...")

    print("func_1 done.......")


def func_2():
    print("func_2 starting......")
    lock_2.acquire()
    print("func_2 申请了lock_2...")
    time.sleep(4)
    print("func_2 等待lock_1...")
    lock_1.acquire()
    print("func_2 申请了lock_1...")

    lock_1.release()
    print("func_2 释放了lock_1...")

    lock_2.release()
    print("func_2 释放了lock_2...")

    print("func_2 done.......")

if __name__ == '__main__':
    print("主线程启动......")
    t1 = threading.Thread(target=func_1, args=())
    t2 = threading.Thread(target=func_2, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("主线程结束了......")