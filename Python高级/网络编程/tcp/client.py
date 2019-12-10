import socket


def main():
    # 1.创建socket
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2.设置地址和端口
    addr = ('127.0.0.1', 8080)
    # 3.连接服务器
    tcp_socket.connect(addr)
    while True:
        # 4.发送消息
        send_msg = input('请输入发送信息:')
        if send_msg == 'exit':
            print('客户端退出')
            break
        tcp_socket.send(send_msg.encode('utf-8'))
        # 5.接收服务器发来数据
        recv_msg = tcp_socket.recv(1024)
        print(recv_msg.decode('utf-8'))
    tcp_socket.close()


if __name__ == '__main__':
    main()
