# LabaDB
![Preview](https://i.imgur.com/Iksme0w.png)
Цель работы - рефлизовать файловую базу данных с графическим интерфейсом на языке Python.

Предметная область базы данных - телефонный справочник, состоящих из 4 полей: номер, фио, возраст, адрес.

# Эффективность алгоритмов

Основой базы данных является словарь Python

## Добавление записи.

Сложность записи элемента в словарь равна O(1). Для двух словарей в два раза больше.

![Insert](https://i.imgur.com/xlAXeqw.png)

## Удаление записи.

Сложность такая же как и добавление записи О(1).

![Delete](https://i.imgur.com/piHtkJU.png)

## Поиск.

Сложность поиска зависит от количества записей с одинаковыми фио. Если дубликатов нет, то О(1).

![Search](https://i.imgur.com/KePnopq.png)

## Запуск
Запустить main.py

## Как реализована работа
Программа написана на языке python с использованием библиотеки PyQt5. Все данные храняться в оперативной памяти в словарях python, которые реалтзованы как хэш-таблицы. Программа может сохранять в формате json, экспортировать и импортировать в csv. Присутсвует все требуемые функции: поиск и удаление по имени, добавление новых записей, сохранение, открытие, экспорт, импорт, требует сохраниение данных, если пользователь может потерять не соххраненные данные.

## Вывод

Реализовал базу данных с графическим интерфейсом, разобрался в принципе работы баз данных.
