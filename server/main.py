import socket
from _thread import *
import datetime

host = '127.0.0.1'
port = 1042
ThreadCount = 0

def client_handler(connection):
    client_mask = '(' + (str(connection)[str(connection).index('raddr=') + 7:])[:-1]
    recv = {'client': client_mask}
    while True:
        data = str(connection.recv(1024), encoding = 'utf8')
        if data == 'disconnect' or not data:
            print('Клиент:', client_mask + ', отключён')
            break
        elif data.find('mess') == 0:
            print(client_mask + ':', data[5:])
        elif data.find('mask') == 0:
            if data.find('edit') == 5:
                client_mask = data[10:]
                recv['client'] = client_mask
            elif data.find('info') == 5:
                recv['<' + str(datetime.datetime.now()) + '> ' + data] = 'Ваш псевдоним: ' + client_mask
            else:
                recv['<' + str(datetime.datetime.now()) + '> ' + data] = 'Команда не распознана'
        elif data.find('acc') == 0:
            print(recv)
            connection.sendall(bytes(recv))
            recv = {'client': client_mask}
        else:
            recv['<' + str(datetime.datetime.now()) + '> ' + data] = 'Команда не распознана'
    connection.close()

def accept_connections(ServerSocket):
    Client, address = ServerSocket.accept()
    print('Принято подключение с: ' + address[0] + ':' + str(address[1]))
    start_new_thread(client_handler, (Client, ))

def start_server(host, port):
    ServerSocket = socket.socket()
    try:
        ServerSocket.bind((host, port))
    except socket.error as e:
        print(str(e))
    print(f'Сервер открыт для поключений на порту {port}...')
    ServerSocket.listen()
    while True:
        accept_connections(ServerSocket)

start_server(host, port)
