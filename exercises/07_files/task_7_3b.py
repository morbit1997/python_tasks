# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
list1 = []
with open('CAM_table.txt') as f:
    for line in f:
        mod_line = line.split()
        if mod_line and mod_line[0].isdigit():
            mod_line.pop(2)
            mod_line[0] = int(mod_line[0])
            list1.append(list(mod_line))
        else:
            continue
list1.sort()
vlan = int(input('Введите vlan: '))
for i in list1:
    if vlan in i:
        print('{:<8} {:10} {:>10}'.format(i[0],i[1],i[2]))