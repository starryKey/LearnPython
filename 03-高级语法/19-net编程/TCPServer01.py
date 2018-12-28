import socket


def tcp_svr():
    #1、建立socket负责具体通信，这个socket其实只负责接受对方的请求，真正通信的是链接后的重新建立的socket
    #需要用到两个参数：
    #AF_INET 含义同UDP一致
    #SOCK_STREAM表明使用的是tcp进行通信
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #2、绑定端口和地址
    #此地址信息是一个元组类型的内容，第一部分为IP，第二部分为端口
    addr2 = ("127.0.0.1", 8996)
    sock.bind(addr2)

    #3、监听接入的访问socket
    sock.listen()

    while True:
        #4、接受访问的socket，可以理解为接受访问即建立了一个通讯的链路
        #accept返回的元组第一个元素赋值给skt，第二个赋值给addr（对方的地址）
        skt,addr3 = sock.accept()

        #5、接受对方发送的内容，利用接收到的socket接收内容
        #500代表接收使用的buffersize
        msf = skt.recv(500)
        #接收到的是bytes格式内容，想要的到str需要进行解码
        msg = msf.decode()

        rst = "Receive msg :{0} from {1} ".format(msg, addr3)
        print(rst)

        #6、如果有必要，给对方发送反馈信息
        skt.send(rst.encode())
        #7、关闭链接通路
        skt.close()

if __name__ == '__main__':
    print("Starting Tcp Servering....")
    tcp_svr()
    print("Ending Tcp Servering....")