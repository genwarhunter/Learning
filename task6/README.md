Задание по "АДМИНИСТРИРОВАНИЕ LINUX И ЗАЩИТА ПУБЛИЧНЫХ СЛУЖБ" <br>
Жариков Константин
==============================
## Вопрос 1: Какие команды позволяет установить задания планировщика?
- `at *время* *дата*`
- `crontab -e *Комманда* `
## Вопрос 2: Что сделает Команда atrm 7?
удаляет задачу с номером 7

## Вопрос 3: Какая команда позволяет установить планировщику crontab задания из файла jobs?
- `crontab jobs `

## Вопрос 4: Когда будет готово задание 19 */2 13 * 5 job.sh? 
- на 19-й минуте каждого четного часа по пятницам 13 

## Вопрос 5: Напишите cron строку установленной на выполнение скрипта job.sh с января по май, в 01:00 по воскресенья
- 0 1 * 1-5 7 job.sh

## Вопрос 6: Просмотреть список всех смонтированных разделов можно командой? 
- ` mount `

## Вопрос 7: описать работу vim (выход, сохранение, поиск, замена строк, удаление строк (полностью частично))
- Выход: `:q`
- Сохранение: `:w`
- Поиск: `\`
- Удалить строку: `D`
- Частично удалить строку: Выбрать курсором нужную часть и нажать `D`

# Практическое задание
## Задание 1: продемонстрировать работу at по запуску задачи записи в файл произвольной строки 
![](https://sun9-17.userapi.com/impf/YapoHY86uGKM3cq27Bi5BbJNpKAGV7kFQFrCrg/nNFVKjTLuyc.jpg?size=582x245&quality=96&sign=f1504c44851d30da648bc15444e929ed&type=album)

## Задание 2: продемонстрировать работу cron по запуску задачи записи в файл произвольной строки  
![](https://sun9-36.userapi.com/impf/PuodJB2ORJZQd1hIKdaZSQpoIKjov0rSd2UKVg/9iSCJUOqJ5c.jpg?size=615x229&quality=96&sign=d485f2781675ed8197ded24e8484c15c&type=album)  
![](https://sun9-57.userapi.com/impf/gOkXJ3HO9-ypo4FxKyK1celRJ1wKwlZ-zpyUUQ/KtD0_z_tJlE.jpg?size=420x95&quality=96&sign=99772b67956cd5f25d5be6d303f35de6&type=album)
![](https://sun9-22.userapi.com/impf/vAXUEf6oilRT5OnNdwdR9t57CDjalJ9ObKGTdQ/FaQ-dvSodWI.jpg?size=373x105&quality=96&sign=0ce57a250dfc51b13df249122c37dc35&type=album)
## Задание 3: примонтировать usb flash и отмонтировать
1. Создаем директорию, куда будем монтировать и смотрим, какие внешние накопители подключены
![](https://sun9-72.userapi.com/impf/PlHSMWmYmOw8oq_6rDca0znmy2l0Na4hxyNk6w/88023fIhxJU.jpg?size=801x633&quality=96&sign=4a49d8f6bef89611a6565d2a05a60fa6&type=album)
2. Монтируем командой `mount *устройство* *место монтирования*`
![](https://sun9-34.userapi.com/impf/-uk4oTm-SMaHLOldzSZs1QSNm9kpt_2-uUnaBg/DQkjjMDYs1s.jpg?size=783x140&quality=96&sign=d7fa877c64c7a8fa150c40f71551bc36&type=album)
3. Размонтируем<br>
![](https://sun9-19.userapi.com/impf/Mu62SnMkMa319AvuWYwpMjP2rXoZYe8sq-sqEA/Ec994UTr3aM.jpg?size=361x84&quality=96&sign=781504fdacade40019a92b454ef2558b&type=album)