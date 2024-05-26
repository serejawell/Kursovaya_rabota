import json

import pytest
from class_operation import Currency, OperationAmount, Operation
from utils import get_class_to_ops_and_sort, get_data, get_executed_operations, get_five_last_executed_operations

@pytest.fixture
def data():
    with open("../data/operations.json") as f:
        data = json.load(f)
    return data

def test_get_data(data):
    assert data is not None





