# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
def get_int_vlan_map(config_filename):
    access_dict = {}
    trunk_dict = {}
    with open(config_filename) as f:
        for line in f:
            if line.startswith('interface'):
                intf = line.split()
                intf = intf[1]
            if line.rstrip().endswith("access"):
                access_dict[intf] = 1
            if 'access vlan' in line:
                vlan = line.split()
                vlan = vlan[3]
                access_dict[intf] = int(vlan)
            elif 'allowed vlan'in line:
                vlan = line.split()
                vlan = vlan[4].split(',')
                for items in range(len(vlan)):
                    vlan[items] = int(vlan[items])
                trunk_dict[intf] = vlan
    dict_tuple = (access_dict,trunk_dict)
    #print(dict_tuple)
    return dict_tuple
print(get_int_vlan_map('config_sw2.txt'))