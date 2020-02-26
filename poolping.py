from datetime import datetime
from multiprocessing import Pool
from pythonping import ping
import ipaddress

# Результаты от pinging(ip) будет добавлять в result_list
result_list = []


def log_result(result):
    """Будет вызываться до тех пор пока метод pinging(ip) возвращает результат,
    result_list изменяется только главным процессом, а не работниками пула.

    :type result: str
    """

    result_list.append(result)


def pinging(ip):
    """Возвращает доступность ip

    :type ip: str
    """

    if ping(ip, count=2).success():
        return '{} - доступно'.format(ip)
    else:
        return '{} - не отвечает'.format(ip)


def main(subnet):
    """Главная функция

    :param subnet: IPv4Network
    """

    print('---Запускаю пинги...')

    # Инициируем экземпляр класса Pool()
    pool = Pool()
    for ipv4 in subnet:
        if ipv4 != subnet[0] and ipv4 != subnet.broadcast_address:
            pool.apply_async(pinging, (str(ipv4),), callback=log_result)
    pool.close()
    pool.join()

    print('---Пинги закончены!')
    print('---Р Е З У Л Ь Т А Т---')
    result_list.sort()
    for r in result_list:
        print(r)


if __name__ == '__main__':
    # Получаем подсеть от пользователя
    subnet = ipaddress.IPv4Network(input('Введите подсеть:'))
    # Фиксируем время начала выполнения скрипта
    time_start = datetime.now()

    # Вызываем главную функцию
    main(subnet)

    # Фиксируем время конца выполнения скрипта
    time_end = datetime.now()
    # Вычитаем из конца - начало и получаем результат
    time_result = time_end - time_start
    print('Скрипт выполнился за: ', time_result)
