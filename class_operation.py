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

    def formation_datetime(self):
        """Метод для форматирования времени из нашего файла json в требуемый"""
        date_object = datetime.fromisoformat(self.date)
        str_dt_obj = date_object.strftime('%d.%m.%y')
        return str_dt_obj

    def card_number_split_and_hide(self, card_infromation):
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
