import socket

True_aliases = [True, 'True', '+', 'true', 'yes', 'Yes', 1, '1']

def processing_echo(echo):
    print(echo)

def mess(HOST, PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print('Соединение успешно установлено')
        while True:
            command = input('Введите команду (CM-client, подключено): ')
            if command.find('send') == 0:
                s.sendall(bytes(command[5:], encoding='utf8'))
            elif command.find('acc') == 0:
                s.sendall(bytes('acc', encoding='utf8'))
                print('История эхо-ответов:', dict(s.recv(1024), encoding = 'utf8'))

def main():
    while True:
        print('Клиент CM запущен успешно')
        command = input('Введите команду (CM-client): ')
        if command.find('start connect') == 0:
            HOST = input('Введите IPv4 сервера: ')
            PORT = int(input('Введите порт сервера: '))
            mess(HOST, PORT)

main()
