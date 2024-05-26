from class_operation import Currency, OperationAmount, Operation
import json

def get_sorted_operations():
    with open('operations.json') as f:
        data = json.load(f)
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
        sorted_operations = sorted(operations, key=lambda x: x.date,  reverse=True)
        return sorted_operations


def get_operations(operations):
    for operation in operations:
        if operation.state == "EXECUTED":
            print(f"""
                {operation.date} {operation.description}
                {operation.join_card_number} -> {operation.to}
                {operation.operation_amount.amount} {operation.operation_amount.currency.name}""")





# def date_sort_operations(operations):
#     operations_list = []
#     for operation in operations:
#         o
#


# def executed_operation():
#     for operation in operations:
#         if operation.state == "EXECUTED":
#             print(operation.info())
#
# print(executed_operation())
