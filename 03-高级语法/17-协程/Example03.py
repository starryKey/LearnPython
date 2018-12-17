# 协程的状态

def simple_code(a):
    print("-> Start")
    b = yield a
    print("-> Received",a,b)

    c = yield a + b
    print("-> received",a,b,c)

# 主线程
sc = simple_code(5)
#预激，然后进入函数simple_code
aa = next(sc)
print(aa)

bb = sc.send(6)
print(bb)

cc = sc.send(7)

print(cc)

