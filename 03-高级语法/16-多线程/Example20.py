

from multiprocessing import Process
import os

def info(title):
    print(title)
    print("module name:", __name__)
    #得到父进程的id
    print("parent process:", os.getppid())
    #得到子进程的id
    print("process id: ", os.getpid())


def func(name):
    info("function f")
    print("Hello", name)

if __name__ == '__main__':

    info("main line")
    p = Process(target=func, args=("jack",))
    p.start()
    p.join()