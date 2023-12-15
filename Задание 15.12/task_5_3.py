# -*- coding: utf-8 -*-
"""
Задание 5.3

Скрипт должен запрашивать у пользователя:
* информацию о режиме интерфейса (access/trunk)
* номере интерфейса (тип и номер, вида Gi0/3)
* номер VLANа (для режима trunk будет вводиться список VLANов)

В зависимости от выбранного режима, на стандартный поток вывода, должна возвращаться
соответствующая конфигурация access или trunk (шаблоны команд находятся в списках
access_template и trunk_template).

При этом, сначала должна идти строка interface и подставлен номер интерфейса, а затем
соответствующий шаблон, в который подставлен номер VLANа (или список VLANов).

Ниже примеры выполнения скрипта, чтобы было проще понять задачу.

Пример выполнения скрипта, при выборе режима access:

Введите режим работы интерфейса (access/trunk): access
Введите тип и номер интерфейса: Fa0/6
Введите номер влан(ов): 3

interface Fa0/6
switchport mode access
switchport access vlan 3
switchport nonegotiate
spanning-tree portfast
spanning-tree bpduguard enable

Пример выполнения скрипта, при выборе режима trunk:
Введите режим работы интерфейса (access/trunk): trunk
Введите тип и номер интерфейса: Fa0/7
Введите номер влан(ов): 2,3,4,5

interface Fa0/7
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan 2,3,4,5
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

interface = {
    "Fa0/1": "Sector-1 connected trunk a-full a-100 10/100BaseTX",
    "Fa0/2": "Sector-2 connected trunk a-full a-100 10/100BaseTX",
    "Fa0/3": "Sector-3 connected trunk a-full a-100 10/100BaseTX",
    "Fa0/4": "notconnect 1 auto auto 10/100BaseTX",
    "Fa0/5": "port connected 100 a-full a-100 10/100BaseTX",
    "Fa0/6": "connected trunk full 100 10/100BaseTX",
    "Fa0/7": "disabled 100 auto auto 10/100BaseTX"
}
template = {"access": access_template, "trunk": trunk_template}

mode = input("Введите режим работы интерфейса (access/trunk): ")
it = input("Введите тип и номер интерфейса: ")
vlans = input("Введите номер влан(ов): ")

print(f"interface {it}")
print("\n".join(template[mode]).format(vlans))