from utils import get_data, get_executing_data, get_format_date, card_number_split_and_hide, get_last_five_operations, get_amount_and_currency

def main():
    data = get_data()
    executed_data = get_executing_data(data)
    operations = get_last_five_operations(executed_data)
    for operation in operations:
        date = get_format_date(operation.get('date'))
        description = operation.get('description')
        by = card_number_split_and_hide(operation.setdefault("from", ""))
        to = card_number_split_and_hide(operation.setdefault('to', ""))
        currency = get_amount_and_currency(operation)
        print(f"""  {date} {description}
        {by} -> {to}
        {currency} \n""")



if __name__ == '__main__':
    main()