import socket


if __name__ == '__main__':
    last_msg = ""
    s = socket.socket()
    host = 'localhost'
    port = 1234

    s.connect((host, port))
    print('client connected')
    while 'down' not in last_msg:
        last_msg = input()
        s.send(bytes(last_msg, 'utf-8'))
        print(s.recv(1024).decode('utf-8'))
    s.close()
    print('client stopped')
