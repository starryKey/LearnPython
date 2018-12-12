import time
import threading

def func():
    print("Start func")
    time.sleep(2)
    print("End func")

print("Main Thread")

t1 = threading.Thread(target=func, args=())
# 设置守护线程的方法，必须在start之前设置，否则无效
t1.setDaemon(True)
# t1.daemon = True
t1.start()

time.sleep(1)
print("Main thread end")