from datetime import datetime
from pythonping import ping
import multiprocessing
import ipaddress

# Результаты от pinging(ip) будет добавлять в result_list
alive_list = []


def log_result(result):
    """Будет вызываться до тех пор пока метод pinging(ip) возвращает результат,
    result_list изменяется только главным процессом, а не работниками пула.

    :type result: str
    """

    if result != 0:
        alive_list.append(result)


def pinging(ip):
    """Возвращает доступную ip

    :type ip: str
    """

    if ping(ip, count=1).success():
        return ip
    else:
        return 0


def main(subnet):
    """Главная функция

    :param subnet: IPv4Network
    """

    # Фиксируем время начала выполнения скрипта
    time_start = datetime.now()

    print('---Запускаю пинги...')

    # Инициируем экземпляр класса Pool(processes=№)
    # Количество процессов у меня на Windows ограничивается в 63 процесса
    # Похоже, для ускорения выполнения скрипта необходимо использовать Semaphor() ограниченный числом ядер в системе
    # ex. pool = multiprocessing.Semaphore(multiprocessing.cpu_count())
    pool = multiprocessing.Pool(processes=60)
    for ipv4 in subnet:
        if ipv4 != subnet[0] and ipv4 != subnet.broadcast_address:
            pool.apply_async(pinging, (str(ipv4),), callback=log_result)
    pool.close()
    pool.join()

    # Фиксируем время конца выполнения скрипта
    time_end = datetime.now()
    # Вычитаем из конца - начало и получаем результат
    time_result = time_end - time_start
    print('---Хосты опрошены за: ', time_result)

    print('---Р Е З У Л Ь Т А Т---')
    print('---Доступные IP---')
    # result_list.sort()
    for r in alive_list:
        print(r)


if __name__ == '__main__':
    # Получаем подсеть от пользователя
    # subnet = ipaddress.IPv4Network(input('Введите подсеть:'))
    subnet = ipaddress.IPv4Network('192.168.88.0/24')

    # Вызываем главную функцию
    main(subnet)
