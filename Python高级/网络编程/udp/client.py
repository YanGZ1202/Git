import socket


def main():
    # 1.创建socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2.设置发送接收的地址
    addr = ('127.0.0.1', 8080)
    end_str = '对方已结束聊天'
    while True:
        # 3.获取发送信息
        send_msg = input('请输入发送信息:')
        if send_msg == 'exit':
            udp_socket.sendto(end_str.encode('utf-8'), recv_addr)
            break
        # 4.发送信息
        udp_socket.sendto(send_msg.encode('utf-8'), addr)
        # 5.接收信息(返回一个元组)-->(收到的消息,('ip地址',端口号))
        recv_msg, recv_addr = udp_socket.recvfrom(1024)
        # 6.打印信息
        print(recv_msg.decode('utf-8'))
        if recv_msg.decode('utf-8') == end_str:
            break
    # 7.关闭socket
    udp_socket.close()


if __name__ == '__main__':
    main()
