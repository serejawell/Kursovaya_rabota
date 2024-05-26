from utils import get_class_to_ops_and_sort, get_data, get_executed_operations, get_five_last_executed_operations

def main():
    operations = get_class_to_ops_and_sort(get_data())
    executed_operations = get_executed_operations(operations)
    get_five_last_executed_operations(executed_operations)


if __name__ == '__main__':
    main()