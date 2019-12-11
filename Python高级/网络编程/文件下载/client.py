import socket


def main():
    # 1.创建socket
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2.设置ip地址和端口
    addr = ('127.0.0.1', 8080)
    # 3.连接服务器
    tcp_socket.connect(addr)
    # 4.输入想要下载的文件名
    file_name = input('请输入下载的文件名:')
    # 5.向服务器发送文件名
    tcp_socket.send(file_name.encode('utf-8'))
    # 6.接收服务器发来的数据
    recv_data = tcp_socket.recv(1024*1024)
    # 7.下载文件
    if recv_data:
        with open('[new]'+file_name, 'wb') as f:
            f.write(recv_data)
    else:
        print('服务器没有改文件')
    # 8.关闭socket
    tcp_socket.close()


if __name__ == '__main__':
    main(

    )