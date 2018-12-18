# 参考资料
 - http://python.jobbole.com/86481/
 - http://python.jobbole.com/87310/
 - https://segmentfault.com/a/1190000009781688
 
 # 迭代器
  - 可迭代(Iterable):直接作用于for循环的变量
  - 迭代器(Iterator):不但可以作用于for循环，还可以被next调用
  - list是典型的可迭代对象，但不是迭代器
  - 案例01
  - 可将可迭代的转为迭代器
  
# 生成器
 - generator：一边循环一边计算下一个元素的机制/算法
 - 需要满足三个条件
    - 每次调用都产生for循环需要的下一个元素或者
    - 如果达到最后一个后，报出StopIteration异常
    - 可以为next函数调用
 - 如何生成一个生成器
    - 直接使用 
    - 如果函数中包含yield，则这个函数就叫生成器
    - next调用函数，遇到yield返回


# 协程
 - 历史
    - 3.4引入协程，用yield实现
    - 3.5引入协程语法
    - 实现的协程比较好用的包有asyncio,tornado,gevent
    
 - 定义：协程是为非抢占式多任务产生子程序的计算机程序组件，协程允许不同入口点在不同位置暂停或开始执行程序
    - 从技术角度讲，协程就是一个你可以暂停执行的函数，或者干脆把协程理解为生成器
 - 协程的实现
    - yield返回
    - send调用
    - 示例02
    
 - 协程的四个状态
    - inspect, getgeneratorstate(...)函数确定，该函数会返回下述字符串中的一个
    - GEN_CREATED:等待开始执行
    - GEN_RUNNING:解释器正在执行
    - GEN_SUSPEND:在yield表达式处暂停
    - GEN_CLOSED:执行结束
    - next预激(prime)
    - 代码示例03
       
 - 协程中止
    - 协程中未处理的异常会向上冒泡，传给next函数或send方法的调用方(即触发协程的对象)
    - 中止协程的一种方式：发送某个哨符值，让协程退出，内置的None和Ellipsis等常量做哨值符==
    
 - yield from
    - 调用协程为了得到返回值，协程必须正常中止
    - 生成器正常中止时会发出StopIteration异常，异常对象的value属性保存返回值
    - yield from 从内部捕获StopIteration异常
    - 案例04
 - 委派生成器
    - 包含yield from表达式的生成器函数
    - 委派生成器在yield from表达式处暂停，调用方可以直接把数据发给子生成器
    - 子生成器再把产生的值发给调用方
    - 子生成器在最后，解释器会抛出StopIteration异常，并且把返回值附件到异常上
    - 案例05
    
# asyncio
 - python3.4开始引入标准库中，内置对异步IO的支持
 - asyncio本身是一个消息循环
    - 步骤：
        - 创建消息循环
        - 把协程导入
        - 关闭
        
        
# async and await
 - 为了更好的表示异步IO
 - Python3.5 引入
 - 让协程代码更简洁
 - 使用上，可以简单的进行替换
    -  用async 替换 @asyncio.coroutine
    - await 替换 yield from 
    
    
# aiohttp 
 - asyncio 实现单线程的并发IO，在客户端用处不大
 - 在服务短可以使用asyncio+ coroutine配合，因为http是IO
 - asyncio实现了tcp、udp、ssl等协议
 - aiohttp 是给予asyncio实现的http框架
 - 安装
    - 执行命令行 pip install aiohttp
    