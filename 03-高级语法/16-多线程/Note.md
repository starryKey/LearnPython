# 文档
 - https://www.cnblogs.com/jokerbj/p/7460260.html
 - http://www.dabeaz.com/python/UnderstandingGIL.pdf
# 多线程 VS 多进程
 - 程序：一堆代码以文本形式存入一个文档
 - 进程：程序运行的一个状态
    - 包含地址空间，内存，数据栈等
    - 每个进程由自己完全独立的运行环境，多进程共享数据是一个问题 
 - 线程
    - 一个进程的独立运行片段，一个进程中可以有多个线程
    - 轻量化的进程
    - 一个进程的多个现成间共享数据和上下文环境
    - 共享互斥问题
 - 全局解析器锁（GIL）
    - Python代码的执行是由python虚拟机进行控制
    - 在主循环中只能有一个控制线程在执行
    
# 线程相关包
  - thread： 有问题，不好用。python3改成_thread
    - 案例01:顺序执行，耗时较长
    - 案例02:改用多线程，缩短总时间，使用_thread
    - 案例03:多线程传参
    
  - threading:通行的使用
    - 直接利用threading.Thread生成Thread实例
        
            
            1、t = threading.Thread(target=xxx, args=(x,x))
            2、t.start()：启动多线程
            3、t.join()：等待多线程执行完成
            4、案例04
            守护线程-daemon
                - 如果在程序中将子线程设置成守护线程，则子线程会在主线程结束的时候自动退出
                - 一般认为，守护线程不重要或者不允许离开主线程独立运行
                - 守护线程案例能否有效跟环境有关
                - 案例05 非守护线程
                - 案例06 守护线程
                
                
    - 线程常用属性
        - threading.currentThread:返回当前线程变量
        - threading.enumerate:返回一个包含正在运行的线程的list，正在运行的线程指的是线程启动后，结束前的线程
        - threading.activeCount:返回正在运行的线程数量，效果同len(threading.enumerate)
        - thr.setName: 给线程设置名字
        - thr.getName:得到线程的名字  
        
  - 直接继承自threading.Thread
       - 直接继承Thread
       - 重写run函数
       - 类实例可以直接运行
       - 案例08
       - 案例09：更工业化的写法
                 