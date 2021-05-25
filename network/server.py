import socket
import concurrent.futures


def conn_process(s: socket.socket):
    c, addr = s.accept()
    last_msg = ''
    print(f"Client from {addr} connected!")
    while 'conn_down' not in last_msg:
        last_msg = c.recv(1024).decode('utf-8')
        print(f"Msg: {last_msg}")
        c.send(bytes(f"Hello from server! Got message: {last_msg}", 'utf-8'))
    c.close()


if __name__ == '__main__':
    s = socket.socket()
    host = 'localhost'
    port = 1234

    s.bind((host, port))
    s.listen()
    last_msg = ""

    print('server is running...')
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as pool:
        pool.map(lambda p: conn_process(s), range(20))
    print('server stopped')
