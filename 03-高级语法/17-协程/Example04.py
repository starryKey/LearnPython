def gen():
    for c in "AB":
        yield c
#list 直接用生成器作为参数
print(list(gen()))

# 多一个中间层

def gen_new():
    for x in "AB":
        yield from x

print(list(gen_new()))
