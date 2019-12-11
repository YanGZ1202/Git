import socket


def main():
    # 1.创建socket
    global send_data

    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2.设置ip和端口
    addr = ('', 8080)
    # 3.绑定ip和端口
    tcp_socket.bind(addr)
    # 4.将socket变为被动
    tcp_socket.listen(128)
    while True:
        send_data = None
        # 5.等待客户端连接
        cli_socket, cli_addr = tcp_socket.accept()
        # 6.接收客户端发来的文件名
        recv_file_name = cli_socket.recv(1024).decode('utf-8')
        # 7.提取文件数据
        try:
            f = open(recv_file_name, 'rb')
            send_data = f.read()
            f.close()
        except Exception as result:
            print(f'没有找到{recv_file_name}文件')
        if send_data:
            # 8.发送数据
            cli_socket.send(send_data)
        # 9.关闭socket
        cli_socket.close()
    tcp_socket.close()


if __name__ == '__main__':
    main()