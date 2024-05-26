from datetime import datetime

class Currency:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class OperationAmount():
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency


class Operation():
    def __init__(self, id, state, date, operation_amount, description, by, to):
        self.id = id
        self.state = state
        self.date = date
        self.operation_amount = operation_amount
        self.description = description
        self.by = by
        self.to = to

    def join_card_number(self):
        pass


