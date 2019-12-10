import socket


def main():
    # 1.创建socket
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2.设置地址和端口
    addr = ('', 8080)
    # 3.绑定地址和端口
    tcp_socket.bind(addr)
    # 4.将socket变为被动
    tcp_socket.listen(128)
    print('等待连接...')
    while True:
        # 5.等待客户端连接
        cli_socket, cli_addr = tcp_socket.accept()
        print(f'{cli_addr[0]}已连接')
        while True:
            # 6.接收数据
            recv_data = cli_socket.recv(1024)
            if recv_data:
                print(f'{cli_addr[0]}:', end='')
                print(recv_data.decode('utf-8'))
                # 7.发送数据给客户端
                send_msg = input('请输入输入消息:')
                cli_socket.send(send_msg.encode('utf-8'))
            else:
                print('客户端已关闭')
                break
        cli_socket.close()
    tcp_socket.close()



if __name__ == '__main__':
    main()
