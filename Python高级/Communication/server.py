import socket


def main():
    # 1.创建socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2.设置地址端口号
    addr = ('127.0.0.1', 8080)
    # 3.绑定接口
    udp_socket.bind(addr)
    end_str = '对方已结束聊天'
    while True:
        # 4.接收消息
        recv_msg, recv_addr = udp_socket.recvfrom(1024)
        # 5.打印信息
        print(recv_msg.decode('utf-8'))
        if recv_msg.decode('utf-8') == end_str:
            break
        # 6.输入发送信息
        send_msg = input('请输入发送消息:')
        if send_msg == 'exit':
            udp_socket.sendto(end_str.encode('utf-8'), recv_addr)
            break
        # 7.发送消息
        udp_socket.sendto(send_msg.encode('utf-8'), recv_addr)
    # 8.关闭socket
    udp_socket.close()


if __name__ == '__main__':
    main()
