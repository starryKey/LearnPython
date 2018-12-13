import threading

sum = 0
loopSum = 1000000
lock = threading.Lock()

def myAdd():
    global sum, loopSum
    for i in range(1, loopSum):
        # 上锁
        lock.acquire()
        sum += 1
        # 解锁
        lock.release()
def myMinu():
    global sum, loopSum
    for i in range(1, loopSum):
        lock.acquire()
        sum -= 1
        lock.release()
if __name__ == '__main__':
    # 非多线程时
    # myAdd()
    # print(sum)
    # myMinu()
    # print(sum)
    print("Starting ...{0}".format(sum))

    # 多线程时
    t1 = threading.Thread(target=myAdd, args=())
    t2 = threading.Thread(target=myMinu, args=())

    t1.start()
    t2.start()
    # 不是原子操作，+ 、- 不是一步完成的，可能还没+上就被-了
    t1.join()
    t2.join()

    print("Done...{0}".format(sum))




