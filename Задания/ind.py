#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    print("help - список всех команд")
    shops = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            product = input("Название продукта: ")
            magazin = input("Магазин: ")
            cost = input("Стоимость товара: ")

            shop = {
                'product': product,
                'magazin': magazin,
                'cost': cost,
            }

            shops.append(shop)
            if len(shops) > 1:
                shops.sort(key=lambda d: d.get('product', ''))

        elif command == 'list':
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
            addedtovar = command[7:]

            count = 0
            for shop in shops:
                if shop.get('product', '') == addedtovar:
                    count += 1
                    print(
                        '{:>4}: {} {}'.format(
                            count, shop.get('magazin', ''),
                            shop.get('cost', '')
                        )
                    )

            if count == 0:
                print("Данный товар не найден.")

        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить товар;")
            print("list - вывести список товаров;")
            print("help - список всех команд;")
            print("exit - завершить работу с программой.")
            print("select... - Получить информацию об определенном товаре")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)

