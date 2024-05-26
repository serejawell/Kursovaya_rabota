from class_operation import Currency, OperationAmount, Operation
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


def get_five_last_executed_operations(operations):
    """Выводит последние 5 успешных операций"""
    for operation in operations[0:5]:
        print(f"""
        {operation.formation_datetime()} {operation.description}
        {operation.card_number_split_and_hide(operation.by)} -> {operation.card_number_split_and_hide(operation.to)}
        {operation.operation_amount.amount} {operation.operation_amount.currency.name}""")


