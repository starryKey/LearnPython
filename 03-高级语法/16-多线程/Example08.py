import threading
import time

# 1、类需要继承自threading.Thread
class MyThread(threading.Thread):
    def __init__(self, arg):
        super(MyThread, self).__init__()
        self.arg = arg
        self.setName("Thr-{0}".format(arg))

    # 2 必须重写run函数，run函数代表的是真正执行的功能
    def run(self):
        time.sleep(2)
        print("The args for this class is {0}".format(self.arg))
        # self.setName("Thr-{0}".format(self.arg))

for i in range(5):
    thr = MyThread(i)
    print("线程名称:{0}".format(thr.getName()))
    thr.start()
    # 等待
    thr.join()
print("Main thread is done......")



