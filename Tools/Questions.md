# Question1 
 - why?:为什么执行过一次迭代后，再迭代时没有值？
 - 原因：迭代器是一个单向的容器，走到末尾之后，不会自动再回到开始的位置，因此再打印时，不会打印任何结果
 - 解决方式：
 
        
        # 解决方式：方法1：遍历map之后，将元素位置恢复到0；方法2：复制两个map对象
        import csv
        import itertools
        参考 https://stackoverflow.com/questions/17416777/why-can-i-only-use-a-reader-object-once)
  