import threading
import time

loop = [4,2]

class ThreadFunc:
    def __init__(self, name):
        self.name = name

    def loop(self, nloop, nsec):
        """

        :param nloop: loop是函数的名称
        :param nsec: 系统休眠时间
        :return:
        """
        print("Start loop", nloop, "at ", time.ctime())
        time.sleep(nsec)
        print("Done loop", nloop, " at ", time.ctime())

def main():

    print("Starting at ", time.ctime())

    # ThreadFunc("loop").loop 跟以下两个式子相等：
    # t = ThreadFunc("loop)
    # t.loop
    # 以下t1和t2的定义方法相等
    t = ThreadFunc("loop")
    t1 = threading.Thread( target=t.loop, args=("LOOP1", 4))
    # 下面的写法更西方人、工业化一些

    t2 = threading.Thread( target=ThreadFunc("loop").loop, args=("LOOP2", 2))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


    print("All dong at ",time.ctime())


# main()

if __name__ == '__main__':
    main()

