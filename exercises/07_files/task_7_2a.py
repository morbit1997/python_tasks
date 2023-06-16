# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт: Скрипт не должен выводить на стандартрый поток вывода команды,
в которых содержатся слова из списка ignore.

При этом скрипт также не должен выводить строки, которые начинаются на !.

Проверить работу скрипта на конфигурационном файле config_sw1.txt.
Имя файла передается как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

from sys import argv

ignore = ["duplex", "alias", "configuration"]
conf_file = argv[1]
flag = 0
with open(conf_file) as f:
    for line in f:
        for ignor in ignore:
            if line.startswith("!"):
                flag = 1
                break
            elif ignor in line:
                flag = 1
                continue
        if flag != 1:
            print(line.rstrip())
        flag = 0