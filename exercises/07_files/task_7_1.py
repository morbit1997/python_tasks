# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
template = '''
Prefix                {}
AD/Metric             {}
Next-Hop              {}
Last update           {}
Outbound Interface    {}
'''
with open('ospf.txt') as f:
    for line in f:
        list1 = line.split(',')
        list2 = list1[0].split()
        list1.pop(0)
        list2.pop(3)
        list2.pop(0)
        list3 = list1 + list2
        list3.insert(3,list3[3][1:7])
        list3.pop(4)
        print(template.format(list3[2],list3[3],list3[4],list3[0].replace(' ',''),list3[1].replace(' ','')))