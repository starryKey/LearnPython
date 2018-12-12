import time
import threading

def func():
    print("Start func")
    time.sleep(2)
    print("End func")

print("Main Thread")

t1 = threading.Thread(target=func, args=())
t1.start()

time.sleep(1)
print("Main thread end")

"""
执行结果
Main Thread
Start func
Main thread end
End func

主线程没了，子线程还在跑
"""