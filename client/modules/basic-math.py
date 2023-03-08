def sqrt(number, **kwargs):
    if kwargs.get('precession', False):
        return round(number ** kwargs.get('degree', 2), kwargs['precession'])
    else:
        return number ** (1 / kwargs.get('degree', 2))

def main():
    func = ['help', 'func', 'start', 'stop']
    print('Добро пожаловать в "Базовую математику"!')
    while True:
        command = input('Введите команду (basic-math): ')
        if command.split(' ')[0] in func:
            if command.find('help') == 0:
                print('Документация по basic-math:')
            elif command.find('start') == 0:
                eval(command[6:])
            elif command.find('func list') == 0:
                print('Список функций basic-math:')
                print('sqrt(number, **degree = 2, precession = None) - при "precession = None" вернёт "number ** (1 / degree)"')
            elif command.find('stop') == 0:
                return 'Спасибо за использование basic-math. Процесс завершён.'
        else:
            print('Команда не распознана.')
