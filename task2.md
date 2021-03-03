Задание по "АДМИНИСТРИРОВАНИЕ LINUX И ЗАЩИТА ПУБЛИЧНЫХ СЛУЖБ" <br> 
Жариков Константин
==============================
## Вопрос 1: Каков размер MBR из чего он состоит?

Размер 512 байт, состоит из:


| Смещение | Длина, байт | Описание |
|----------------|:---------:|----------------:| 
| 0000h | 446 | Код загрузчика |
| 01BEh | 16 | Раздел 1 |
| 01CEh | 16 | Раздел 2 |
| 01DEh | 16 | Раздел 3 |
| 01EEh | 16 | Раздел 4 |
| 01FEh | 2 | Сигнатура |

## Вопрос 2: Сколько разделов поддерживает MBR:

4

## Вопрос 3: Описать процесс загрузки все этапы на BIOS и UEFI
### bios
1. Этап инициализации и проверки оборудования
2. Загрузка в режиме BIOS
3. Загрузка модуля поддержки совместимости
4. Запуск загрузчика ОС LEGACY BIOS

### UEFI
1. Security Phase
2. Pre-EFI Initialization
3. Среда для исполнения драйверов
4. Boot Device Select
5. Transient System Load
6. Runtime

## Вопрос 4: описать порядок загрузки ОС на sysVinit и systemd
### 
Как init, так и systemd — это демоны (фоновые процессы — службы), которые управляют другими демонами, поскольку первая служба запускается (во время загрузки) и последняя служба заканчивается (во время выключения). Для этого запускаются стартовые сценарии, которые выполняют проверку и монтирование файловых систем, запуск необходимых демонов, настройку ядра (в том числе загрузку модулей ядра согласно установленному оборудованию, настройку IP-адресов, таблиц маршрутизации и другие задачи), запуск графической оболочки. 
### Systemd: 
Systemd запускает сервисы описанные в его конфигурации.Конфигурация состоит из множества файлов, которыепо-модному называют юнитами.
Все эти юниты разложены в трех каталогах:
- /usr/lib/systemd/system/ – юниты из установленныхпакетов RPM — всякие nginx, apache, mysql и прочее
- /run/systemd/system/ — юниты, созданные в рантайме —тоже, наверное, нужная штука
- /etc/systemd/system/ — юниты, созданные системнымадминистратором — а вот сюда мы и положим свой юнит.


## Вопрос 5: показать скриншоты вашего используемого Linux дистрибутива и объяснить на какой системе инициализации он работает

![](https://sun9-14.userapi.com/impf/tiJ59I6kv6X7-EgOwZ9024vUBBOCrY-q4nQWCQ/B7-mU-SAgk0.jpg?size=800x149&quality=96&sign=f08df05230904256d8ea445f03f443ff&type=album)


## Вопрос 6: Точка монтирования - это?

файл или каталог, с помощью которого осуществляется доступ к новой файловой системе, файлу или каталогу

## Вопрос 7: Символом "-" обозначается тип файла?
Обычный файл

## Вопрос 8: Текущее положение в файловой системе можно просмотреть командой?
```pwd```

## Вопрос 9: Как сделать рекурсивное копирование каталога?
```cp -R```

## Вопрос 10: Какие команды предназначены для создания элементов файловой системы
1. создание каталога:
- ```mkdir *имя каталога*```

2. создание файла:
- ```touch *имя файла*```
- ```cat > *имя файла*```
- ```echo > *имя файла*```
- ```> *имя файла*```

## Вопрос 11: Домашний каталог суперпользователя находится по адресу?
/root