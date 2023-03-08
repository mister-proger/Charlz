import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 1042         # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        s.sendall(bytes(input(), encoding='utf8'))

# -----

import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 1042       # Port to listen on (non-privileged ports are > 1023)

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Соединение с', addr)
            while True:
                data = str(conn.recv(1024))
                data = data[2:]
                data = data[:-1]
                print(data)
