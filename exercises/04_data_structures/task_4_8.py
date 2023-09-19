# -*- coding: utf-8 -*-
"""
Завдання 4.8

Перетворити IP-адресу в змінній ip на двійковий формат і вивести на стандартний
потік виведення вивід стовпцями, таким чином:
* першим рядком повинні йти десяткові значення байтів
* другим рядком двійкові значення

Вивід має бути впорядкований також, як у прикладі:
* стовпцями
* ширина стовпця 10 символів (у двійковому форматі треба додати два пробіли між
  стовпцями для поділу октетів між собою)

Приклад для адреси 10.1.1.1:
10        1         1         1
00001010  00000001  00000001  00000001

Попередження: у розділі 4 тести можна легко "обдурити", зробивши потрібний
вивід print, без отримання результатів з даних завдання за допомогою Python. Це
не означає, що завдання зроблено правильно, просто на даному етапі складно
інакше перевіряти результат.
"""

ip = "192.168.3.1"
