# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости
от выбранного режима, задавались разные вопросы в запросе о номере
VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]
interface_workmode = str(input("Введите режим работы интерфейса: "))
interface_numtype = input("Введите номер интерфейса: ")
#allow_vlan = input('Введите разрешенные VLANы:')
d1 = dict(access = access_template, trunk = trunk_template)
d2 = dict(access = "Введите номер VLAN: ", trunk = 'Введите разрешенные VLANы: ')
vlan_num = input(d2[interface_workmode])
print('interface {}'.format(interface_numtype))
print('\n'.join(d1[interface_workmode]).format(vlan_num))