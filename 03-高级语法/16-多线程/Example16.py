import threading
import time

def func():
    print(" is running......")
    time.sleep(4)
    print(" is done......")

if __name__ == '__main__':
    # 多长时间后调用该函数
    t = threading.Timer(6, func)
    t.start()

    i = 0
    while True:
        print("{0}********".format(i))
        time.sleep(3)
        i += 1

        if i == 5:
            t.cancel()
            break

