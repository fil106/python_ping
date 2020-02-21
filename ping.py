from datetime import datetime
from pythonping import ping
import ipaddress

#Получаем подсеть от пользователя
user_subnet = ipaddress.ip_network(input('Что пингуем?:'))
#Фиксируем время начала выполнения скрипта
time_start = datetime.now()

print ('---Запускаю пинги...')
for ip in user_subnet:

	if ip == user_subnet[0]:
		print (str(ip) + ' - сеть')
		continue
	elif ip == user_subnet.broadcast_address:
		print (str(ip) + ' - широковещательный адрес')
		continue
	
	# Результат пинга помещаем в response_list
	response_list = ping(str(ip), count=2)

	if response_list.success():
		print (str(ip) + ' - доступен')
	else:
		print (str(ip) + ' - недоступен')
print ('---Пинги закончены!')

#Фиксируем время конца выполнения скрипта
time_end = datetime.now()
#Вычитаем из конца - начало и получаем результат
time_result = time_end - time_start
print ('Скрипт выполнился за: ', time_result)
