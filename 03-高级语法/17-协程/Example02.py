# 协程代码案例

def simple_code():
    print("-> Start")
    x = yield
    print("-> received",x)

# 主线程
sc = simple_code()
print(11111)
# 可以使用sc.send(None)，效果一样
next(sc) #预激

print(2222)
sc.send("Test end")

