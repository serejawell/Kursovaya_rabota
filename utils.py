from class_operation import Currency, OperationAmount, Operation
from datetime import datetime
import json


def get_data():
    """Открываем наш json"""
    with open('data/operations.json') as f:
        data = json.load(f)
        return data

def get_class_to_ops_and_sort(data):
    """Согласно полям класса распределяем все данные"""
    operations = []
    for item in data:
        currency = Currency(
            name=item.get("operationAmount", {}).get("currency", {}).setdefault("name", ""),
            code=item.get("operationAmount", {}).get("currency", {}).setdefault("code", "")
        )
        operation_amount = OperationAmount(
            amount=item.get("operationAmount", {}).setdefault("amount", ""),
            currency=currency
        )

        operation_main = Operation(
            id=item.setdefault("id", ""),
            state=item.setdefault("state", ""),
            date=item.setdefault("date", ""),
            operation_amount=operation_amount,
            description=item.setdefault("description", ""),
            by=item.setdefault("from", ""),
            to=item.setdefault("to", "")
        )
        operations.append(operation_main)
    sorted_operations = sorted(operations, key=lambda x: x.date, reverse=True)
    return sorted_operations


def get_executed_operations(operations_list):
    """Функция показывает данные об успешных операциях"""
    executed_list = []
    for operation in operations_list:
        if operation.state == "EXECUTED":
            executed_list.append(operation)
    return executed_list


def formation_datetime(date):
    """Метод для форматирования времени из нашего файла json в требуемый"""
    date_object = datetime.fromisoformat(date)
    str_dt_obj = date_object.strftime('%d.%m.%y')
    return str_dt_obj

def card_number_split_and_hide(card_infromation):
    """В этом методе мы разделяем наш счет на название карты и номер для удобной работы с ними, в
    последующих действиях этот метот можно будет применить к from и to. Также мы не трогаем счет, и закрываем
    нужное кол-во цифр звездочками для секретности"""
    if "Счет" in card_infromation:
        return "Счет **{}".format(card_infromation[-4:])
    else:
        card_info = card_infromation.split(" ")
        card_name = []
        for card in card_info:
            if card.isalpha():
                card_name.append(card)
            elif card.isdigit():
                card_number = " ".join([card[i:i + 4] for i in range(0, len(card), 4)])
                card_number = "{}** **** {}".format(card_number[:7], card_number[-4:])
                card_name.append(card_number)
        return " ".join(card_name)


def get_five_last_executed_operations(operations):
    """Выводит последние 5 успешных операций"""
    for operation in operations[0:5]:
        print(f"""{formation_datetime(operation.date)} {operation.description}
        {card_number_split_and_hide(operation.by)} -> {card_number_split_and_hide(operation.to)}
        {operation.operation_amount.amount} {operation.operation_amount.currency.name}""")
        print("")


