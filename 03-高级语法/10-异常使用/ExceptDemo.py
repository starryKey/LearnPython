#异常案例
#出错后给出提示
"""
案例01

try:
    num = int(input("please input your number:"))
    rst = 100 / num
    print("计算的结果是:{0}".format(rst))
# 捕获异常后，把异常实例化，输出信息会在实例中
except ZeroDivisionError as err:
    print("计算出错了")
    #exit推出程序
    print(err)
    exit()
except NameError as err:
    print("名字写错了")
    print(err)
except AttributeError as err:
    print("属性有问题")
    print(err)
# 所有的异常都是继承自Exception类
# 使用以下代码，任何异常都会捕获
except Exception as err:
    print(err)

"""


#raise案例 02
try:
    print("测试主动抛出异常")
    # raise 后面跟异常类
    raise ValueError
    print("测试")
except NameError as err:
    print("NameError")
except ValueError as err:
    print("Value error")
except Exception as err:
    print("有异常")
finally:
    print("不管有没有异常都会执行我的")


# 所有的异常都是继承自Exception类，可以自定义异常
# 自定义异常 案例03
class testError(Exception):
    def __init__(self,arg):
        self.args = arg
try:
    raise testError("Just error")
except testError as err:
    print(err)

# else执行案例

try:
    num = int(input("please input your number:"))
    rst = 100 / num
    print("计算的结果是:{0}".format(rst))
except Exception as err:
    print(err)
else:
    print("没有错误哦")
finally:
    print("反正我都会执行的 哈哈哈😂")
