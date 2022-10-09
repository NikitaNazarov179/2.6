#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    print("help - список всех команд")
    # Список товаров.
    shops = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о человеке.
            product = input("Название продукта: ")
            magazin = input("Магазин: ")
            cost = input("Стоимость товара: ")

            # Создать словарь.
            shop = {
                'product': product,
                'magazin': magazin,
                'cost': cost,
            }

            # Добавить словарь в список.
            shops.append(shop)
            # Отсортировать список в случае необходимости.
            if len(shops) > 1:
                shops.sort(key=lambda d: d.get('product', ''))

        elif command == 'list':
            # Заголовок таблицы.
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 15
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
                    "№",
                    "Товар",
                    "Магазин",
                    "Стоимость товара"
                )
            )
            print(line)

            # Вывести данные о всех товарах.
            for idx, shtuka in enumerate(shops, 1):
                print(
                    '| {:^4} | {:<30} | {:<20} | {:<15} |'.format(
                        idx,
                        shtuka.get('product', ''),
                        shtuka.get('magazin', ''),
                        shtuka.get('cost', ''),
                        ' ' * 5
                    )
                )

            print(line)

        elif command.startswith('select '):
            # Получить введенный товар
            addedtovar = command[7:]

            # Инициализировать счетчик.
            count = 0
            # Проверить сведения работников из списка.
            for shop in shops:
                if shop.get('product', '') == addedtovar:
                    count += 1
                    print(
                        '{:>4}: {} {}'.format(
                            count, shop.get('magazin', ''),
                            shop.get('cost', '')
                        )
                    )

            # Если счетчик равен 0, то работники не найдены.
            if count == 0:
                print("Данный товар не найден.")

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить товар;")
            print("list - вывести список товаров;")
            print("help - список всех команд;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)

