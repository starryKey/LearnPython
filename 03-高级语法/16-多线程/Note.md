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
  - threading:通行的包
  - 案例01