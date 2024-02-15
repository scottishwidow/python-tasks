# -*- coding: utf-8 -*-
"""
Завдання 4.6

Обробити рядок ospf_route та вивести інформацію на стандартний потік виведення у вигляді:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Для цього використовувати шаблон template і підставити значення з рядка
ospf_route. Значення рядка ospf_route треба отримати за допомогою Python.

Попередження: у розділі 4 тести можна легко "обдурити", зробивши потрібний
вивід print, без отримання результатів з даних завдання за допомогою Python. Це
не означає, що завдання зроблено правильно, просто на даному етапі складно
інакше перевіряти результат.
"""

ospf_route = "10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"

parts = ospf_route.split()

prefix = parts[0]
ad_metric = parts[1].strip("[]")
next_hop = parts[3].strip(",")
last_update = parts[4].strip(",")
outbound_interface = parts[5]

template = """

Prefix                {}
AD/Metric             {}
Next-Hop              {}
Last update           {}
Outbound Interface    {}

"""

output = template.format(prefix, ad_metric, next_hop, last_update, outbound_interface)

print(output)
