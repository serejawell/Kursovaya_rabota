from datetime import datetime


class Currency:
    """Аналогично классу OperationAmount"""

    def __init__(self, name, code):
        self.name = name
        self.code = code


class OperationAmount:
    """Создание класса для удобной работы с json со своими методами"""

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency


class Operation:
    """Создаем базовый класс с его методами"""

    def __init__(self, id, state, date, operation_amount, description, by, to):
        self.id = id
        self.state = state
        self.date = date
        self.operation_amount = operation_amount
        self.description = description
        self.by = by
        self.to = to



