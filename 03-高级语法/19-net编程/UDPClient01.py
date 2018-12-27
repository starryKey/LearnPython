"""
- Client端流程
    - 1、建立通信的socket
    - 2、发送内容到指定的服务器
    - 3、接受服务器给定的反馈内容

"""

import socket

def clientFunc():

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    text = "I miss you"

    #发送的数据必须是bytes格式

    data = text.encode()

    # 发送
    sock.sendto(data, ("127.0.0.1", 7666))

    data, addr = sock.recvfrom(200)

    data = data.decode()

    print(data)

if __name__ == '__main__':
    clientFunc()