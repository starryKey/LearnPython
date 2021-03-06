"""
利用time函数，生成两个函数
顺序调用
计算总的运行时间

"""
import time
import _thread

def loop1():
    print("Start loop 1 at :",time.ctime())
    time.sleep(2)
    print("End loop 1 at :",time.ctime())

def loop2():
    print("Start loop 2 at :",time.ctime())
    time.sleep(1)
    print("End loop 2 at :",time.ctime())

def main():
    print("Starting at :",time.ctime())
    # 启动多线程的意思是用多线程去执行某个函数
    # 启动多线程的函数是start_new_thread
    # 参数两个，第一个是需要运行的函数名，第二个是函数的参数作为元组使用
    # 注意，如果函数只有一个参数，需要参数后有一个逗号，
    _thread.start_new_thread(loop1, ())
    _thread.start_new_thread(loop2, ())
    print("All done at :", time.ctime())

if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)



# 使用线程实现

