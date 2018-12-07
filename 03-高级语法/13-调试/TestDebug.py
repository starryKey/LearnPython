def sayHello(name):
    print("haha, I want to say hello with you,{0}".format(name))
    print("hello,{0}".format(name))
    print("Done......")

if __name__ == "__main__":
    print("***" * 10)
    name = input("please input your name: ")
    print(sayHello(name=name))
    print("***" * 10)
# step over 跳过  此时sayHello当一句代码执行
# step into 进去  此时进入sayHello中
# step out 跳出去