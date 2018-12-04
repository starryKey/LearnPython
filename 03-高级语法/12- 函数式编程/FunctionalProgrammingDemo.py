# 01 lambda表达式
#一个参数

stm = lambda x:100 * x
res1 = stm(10)
print(res1)
# 多个参数
stm2 = lambda x,y,z:x + y * 10 + z * 100
res2 = stm2(2,3,4)
print(res2)

print("*" * 15 +  "我是分割符" + "*" * 15)

# 02 高阶函数

# 变量可以赋值
a = 100
b = a
# 函数名称就是一个变量
def funcA():
    print("I am funcA")
funcA()
print(funcA)
funcB = funcA
print(funcB)