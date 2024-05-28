import json
from datetime import datetime


def get_data():
    """Открываем наш json"""
    with open('data/operations.json') as f:
        data = json.load(f)
        return data


def get_executing_data(data):
    """Забираем успешные операции, с помощью datetime преобразуем дату"""
    new_operations_list = []
    for operations in data:
        if operations and operations.get('date') is not None and operations.get('state') == 'EXECUTED':
            operations['date'] = datetime.fromisoformat(operations['date'])
            new_operations_list.append(operations)
    return new_operations_list


def get_format_date(date):
    """Форматируем нашу дату в требуемую"""
    return date.strftime('%d.%m.%Y')


def card_number_split_and_hide(card_information):
    """В этом методе мы разделяем наш счет на название карты и номер для удобной работы с ними, в
    последующих действиях этот метот можно будет применить к from и to. Также мы не трогаем счет, и закрываем
    нужное кол-во цифр звездочками для секретности"""
    if "Счет" in card_information:
        return "Счет **{}".format(card_information[-4:])
    else:
        card_info = card_information.split(" ")
        card_name = []
        for card in card_info:
            if card.isalpha():
                card_name.append(card)
            elif card.isdigit():
                card_number = " ".join([card[i:i + 4] for i in range(0, len(card), 4)])
                card_number = "{}** **** {}".format(card_number[:7], card_number[-4:])
                card_name.append(card_number)
        return " ".join(card_name)


def get_last_five_operations(data):
    """Сортировка по убыванию дат, оставляем 5 последних операций"""
    return sorted(data, key=lambda x: x['date'], reverse=True)[:5]


def get_amount_and_currency(operation):
    """Возвращаем стоимость и валюту"""
    amount = operation['operationAmount']['amount']
    currency = operation['operationAmount']['currency']['name']
    return f'{amount} {currency}'
