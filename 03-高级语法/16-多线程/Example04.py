"""
利用time函数，生成两个函数
顺序调用
计算总的运行时间

"""
# 带参数
import time
import threading

def loop1(n1):
    print("Start loop 1 at :",time.ctime())
    print("loop1 参数1:{0}".format(n1))
    time.sleep(2)
    print("End loop 1 at :",time.ctime())

def loop2(n1,n2):
    print("Start loop 2 at :",time.ctime())
    print("loop2 参数1：{0},参数2：{1}".format(n1, n2))
    time.sleep(1)
    print("End loop 2 at :",time.ctime())

def main():
    print("Starting at :",time.ctime())
    # 启动多线程的意思是用多线程去执行某个函数
    # 启动多线程的函数是start_new_thread
    # 参数两个，第一个是需要运行的函数名，第二个是函数的参数作为元组使用
    # 注意，如果函数只有一个参数，需要参数后有一个逗号，
    t1 = threading.Thread(target=loop1, args=("我是参数1",))
    t1.start()
    t2 = threading.Thread(target=loop2, args=("我是参数1","我是参数2"))
    t2.start()
    # 等待多线程执行完，使用join后，打印3最后执行，否则不是
    t1.join()
    t2.join()
    print("打印3 All done at :", time.ctime())

if __name__ == '__main__':
    main()
    # 一定要有while语句
    # 因为启动多线程后本程序就作为主线程存在
    # 如果主线程执行完毕，则子线程可能也需要中止
    while True:
        time.sleep(10)


