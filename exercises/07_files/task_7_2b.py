# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
from sys import argv
ignore = ["duplex", "alias", "configuration"]

conf_file = argv[1]
dest_file = argv[2]
flag = 0
with open(conf_file) as f, open(dest_file, 'w') as f2:
    for line in f:
        for ignor in ignore:
            if line.startswith("!"):
                flag = 1
                break
            elif ignor in line:
                flag = 1
                continue
        if flag != 1:
            f2.write(line)
        flag = 0