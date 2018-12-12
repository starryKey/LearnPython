

import time
import threading

def loop1():
    #ctimed当前时间
    print("Start loop 1 at :",time.ctime())
    time.sleep(4)
    print("End loop 1 at :",time.ctime())

def loop2():
    print("Start loop 2 at :",time.ctime())
    time.sleep(2)
    print("End loop 2 at :",time.ctime())
def loop3():
    print("Start loop 3 at :", time.ctime())
    time.sleep(5)
    print("End loop 3 at :", time.ctime())

def main():
    print("Start at: ",time.ctime())
    #生成threading.Thread实例
    t1 = threading.Thread(target=loop1, args=())
    t1.setName("Thr-1")
    t1.start()

    t2 = threading.Thread(target=loop2, args=())
    t2.setName("Thr-2")
    t2.start()

    t3 = threading.Thread(target=loop3, args=())
    t3.setName("Thr-3")
    t3.start()

    # 预期三秒后，Thr-2结束
    time.sleep(3)

    for thr in threading.enumerate():
        print("正在运行的线程名称为:{0}".format(thr.getName()))

    print("正在运行的子线程个数为:{0}".format(threading.activeCount()))
    print("Al done at :", time.ctime())

main()