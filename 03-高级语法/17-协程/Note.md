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
