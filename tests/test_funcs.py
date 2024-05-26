import pytest
import json
from datetime import datetime
from class_operation import Currency, OperationAmount, Operation
from utils import get_data, get_class_to_ops_and_sort, get_executed_operations, get_five_last_executed_operations

# Mock data similar to operations.json


@pytest.fixture
def mock_operations():
    mock_data = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        },
        {
            "id": 464419177,
            "state": "CANCELED",
            "date": "2018-07-15T18:44:13.346362",
            "operationAmount": {
                "amount": "71024.64",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "Visa Gold 9657499677062945",
            "to": "Счет 19213886662094884261"
        }
    ]
    return mock_data

def test_get_data(monkeypatch):
    def mock_open(*args, **kwargs):
        return mock_operations()
    monkeypatch.setattr('builtins.open', mock_open)
    data = get_data()
    assert len(data) == 3

def test_get_class_to_ops_and_sort(mock_operations):
    data = get_class_to_ops_and_sort(mock_operations)
    assert len(data) == 3
    assert isinstance(data[0], Operation)
    assert data[0].date > data[-1].date

def test_get_executed_operations(mock_operations):
    data = get_class_to_ops_and_sort(mock_operations)
    executed_ops = get_executed_operations(data)
    assert len(executed_ops) == 2
    for op in executed_ops:
        assert op.state == "EXECUTED"

def test_get_five_last_executed_operations(capsys, mock_operations):
    data = get_class_to_ops_and_sort(mock_operations)
    executed_ops = get_executed_operations(data)
    get_five_last_executed_operations(executed_ops)
    captured = capsys.readouterr()
    assert "Перевод организации" in captured.out