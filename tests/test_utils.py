import pytest
from datetime import datetime
from utils import get_data, get_executing_data, get_format_date, card_number_split_and_hide, get_last_five_operations, \
    get_amount_and_currency


@pytest.mark.parametrize('list_dict, expected', [
    ([{}], []),
    ([{"date": "2019-04-04T23:20:05.206878", "state": "EXECUTED"}],
     [{"date": datetime.fromisoformat("2019-04-04T23:20:05.206878"), "state": "EXECUTED"}]),
    ([{"date": "2019-04-04T23:20:05.206878"}], []),
    ([{"state": "EXECUTED"}], []),
])
def test_get_executing_data(list_dict, expected):
    assert get_executing_data(list_dict) == expected


def test_get_data():
    with pytest.raises(FileNotFoundError):
        get_data()


def test_get_last_five_operations():
    assert get_last_five_operations([]) == []
    assert get_last_five_operations([
        {'date': 2},
        {'date': 3},
        {'date': -5},
        {'date': 11},
        {'date': 0},
        {'date': 4}
    ]) == [{'date': 11}, {'date': 4}, {'date': 3}, {'date': 2}, {'date': 0}]


def test_get_format_date():
    with pytest.raises(AttributeError):
        get_format_date('05.10.24?')
    assert get_format_date(datetime.fromisoformat("2018-02-22T00:40:19.984219")) == '22.02.2018'


def test_card_number_split_and_hide():
    assert card_number_split_and_hide("Счет 54883981902864782073") == 'Счет **2073'
    assert card_number_split_and_hide("Visa Classic 3414396880443483") == 'Visa Classic 3414 39** **** 3483'
    assert card_number_split_and_hide(None) == 'None'


def test_get_amount_and_currency():
    assert get_amount_and_currency({
        "id": 260972664,
        "state": "EXECUTED",
        "date": "2018-01-23T01:48:30.477053",
        "operationAmount": {
            "amount": "2974.30",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        }
    })
