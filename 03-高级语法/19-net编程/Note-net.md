# 网络编程

## 网络协议：一套规则

## 网络模型
 - 七层网络模型(OSI参考模型)
    - 应用层
    - 表示层
    - 会话层
    - 传输层
    - 网络层
    - 数据链路层
    - 物理层
 -  TCP/IP五层模型
    - 应用层  （HTTP Telnet FTP TFTP DNS SMTP）
    - 传输层   (TCP UDP)
    - 网络层   (IP ICMP RIP IGMP)
    - 数据链路层(ARP RARP IEEE*02.3 PPP CSMA/CD)
    - 物理层    (FE自协商 Manchester MLT-3 4A PAMS)
    
 - 每一层都有相应的协议负责交换信息或者协同工作
 - TCP/IP 协议族
 - IP地址：负责在网络上唯一定位一个机器
    - IP地址分ABCDE类
    - 是由四个数字段组成，每个数字段的取值是0-255
    - 192.168.xxx.xxx：局域网IP
    - 127.0.0.1:本机
    - IPV4,IPV6
 - 端口
    - 范围：0-65535
        - 知名端口:0-1023
        - 非知名端口:1024-
        
## TCP/UDP协议
 - UDP:非安全的不面向链接的传输
    - 安全性差
    - 大小限制64kb
    - 没有顺序
    - 速度快
    - 示例：即时通讯
    
 - TCP：基于链接的通信
    - 安全
    
## Socket编程
 - IP通信，端口通信
 - socket(套接字)：是一个网络通信的端点，能实现不同主机的进程通信，网络大多数通过Socket完成
 - 通过IP+端口定位对方并发送消息的通信机制
 - 分为UDP和TCP
 - 客户端Client:发起访问的一方
 - 服务端Server:接受访问的一方
 
### UDP编程
 - Server端流程
    - 1、建立socket，socket是负责具体通信的一个实例
    - 2、绑定，为创建的socket指派固定的端口和IP地址
    - 3、接受对方发送的内容
    - 4、给对方发送反馈，此步骤为非必须步骤
 - Client端流程
    - 1、建立通信的socket
    - 2、发送内容到指定的服务器
    - 3、接受服务器给定的反馈内容
 - 示例
    - 服务器案例UDPServer01
    - 客户端案例UDPClient01
    - 服务器程序要求永久运行，一般用死循环处理
    - 改造的服务器版本Server02
    

### TCP编程
 - 面向链接的传输，即每次传输之前需要建立一个链接
 - 客户端和服务端两个程序要编写
 - Server端的编写流程
    - 1、建立socket负责具体通信，这个socket其实只负责接收对方的请求
    - 2、绑定端口和地址
    - 3、监听接入访问的socket
    - 4、接收访问的socket，可以理解为接收访问即建立了一个通讯的链接通路
    - 5、接受对方的发送内容，利用接受到的socket接受内容
    - 6、如果有必要，给对方发送反馈消息
    - 7、关闭链接通路
 - Client端流程
    - 1、建立通信socket
    - 2、链接对方，请求跟对方建立通路
    - 3、发送内容到对方服务器
    - 4、接受对方的反馈
    - 5、关闭链接通路
 - 案例TCPClient01，TCPServer01
    
    
### FTP编程
 - TFP(FileTransferProtocol)文件传输协议
 - 用途：定制一些特殊的上传下载文件的服务
 - 用户分类：登录FTP服务器必须有一个账号
    - Real用户：注册账户
    - Guest账户：可能临时对某一类人的行为进行授权
    - Anonymous:匿名账户，允许任何人
 - FTP工作流程
    - 1、客户端链接远程主机上的FTP服务器
    - 2、客户端输入用户名和密码(或者anonymous)和电子邮件地址
    - 3、客户端和服务器进行各种文件传输和信息查询操作
    - 4、客户端从远程服务器退出，结束传输
    
 - FTP文件表示
    - 分三段表示FTP服务器上的文件
    - HOST：主机地址，类似于ftp.mozilla,org,以ftp开头
    - DIR:目录，表示文件所在本地的路径，例如:pub/android/focus/
    - File:文件名称，如Klar-1,1-RC1.apk
    - 如果想完整精确表示ftp上的某个文件，需要上述三部分组合在一起
    - 示例ftp01
    
    
### Mail编程
 - 资料
    - [官网](https://docs.python.org/3/library/email.html)
 - 邮件工作流程
    - MUA(MailUserAgent)邮件用户代理
    - MTA(MailTransferAgent)邮件传输代理
    - MDA(MailDeliveryAgent)邮件投递代理
    - testfrom@qq.com
    - testto@sina.com
    - 流程
        - 1、MUA->MTA, 邮件已经在服务器上了
        - 2、qq MTA->.........->sina MTA, 邮件在新浪的服务器上
        - 3、sina MTA-> sina MDA, 此时邮件已经在你的邮箱里了
        - 4、sina MDA -> MUA(Foxmail/Outlook), 邮件下载到本地电脑
    - 编写程序
        - 发送：MUA->MTA with SMTP:SimpleMailTransferProtocal，包含MTA->MTA
        - 接收：MDA->MUA with POP3 and IMAP：PostOfficeProtocal v3 and InternetMessageAccessProtocal v4
    - 准备工作
        - 注册邮箱（QQ邮箱为例）
        - 第三方邮箱需要特殊设置， 以qq邮箱为例
            - 进入设置中心
            - 取得授权码
    - Python for mail 
        - SMTF协议负责发送邮件
            - 使用mail模块构建邮件
                - 纯文本邮件
                - MailExample01 
            - HTML格式邮件发送
                - 准备HTML代码作为内容
                - 把邮件的subtype设为html
                - 发送
                - MailExample02 
            - 发送带附件的邮件
                - 可以把邮件看作是一个文件邮件和一个附件的合体
                - 一封邮件如果涉及多个部分，使用MIMEMultipart格式构建
                - 添加一个MIMEText正文
                - 添加一个MIMEBase或者MIMEText作为附件
                - EmailExample03
            - 添加邮件头，抄送信息等
                - mail["From"] 表示发送者信息，包括姓名和邮件
                - mail["To"] 表示接收者信息，包括姓名和邮件地址
                - mail["Subject"] 表示摘要或者主题信息
                - MailExample04
            - 同时支持html和text格式
                - 构建一个MIMEMultipart格式邮件
                - MIMEMultipart的subtype设置成alternative格式  
                - 添加HTML和text邮件
                - MailExample05
                  
            - 使用smtplib模块发送邮件
            
        - POP3协议接收邮件
            - 本质上是MDA到MUA的一个过程
            - 从 MDA下载下来的是一个完整的邮件结构体，需要解析才能得到每个具体可读的内容
            - 步骤：
                - 用poplib下载邮件结构体原始内容
                - 准备相应的内容（邮件地址，密码，POP3实例）
                - 身份认证
                - 一般会先得到邮箱内邮件的整体列表
                - 根据相应序号，得到某一封信的数据流
                - 利用解析函数进行解析出相应的邮件结构体
                - 用email解析邮件的具体内容
                - MailExample06      
    
 

