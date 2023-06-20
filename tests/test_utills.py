import pytest
from src.utills import get_data, get_filtered_data, get_last_values, get_formatted_data, encode_bill_info


def test_get_data():
    data = get_data()
    assert isinstance(data, list)


def test_get_filtered_data(test_data):
    data = get_filtered_data(test_data)
    assert len(data) == 3


def test_get_last_values(test_data):
    data = get_last_values(test_data, 4)
    assert [x['date'] for x in data] == ['2019-08-26T10:50:58.294041', '2019-07-03T18:35:29.512364', '2019-04-04T23:20:05.206878', '2019-03-23T01:09:46.296404']



def test_formatted_data(test_data):
    data = get_formatted_data(test_data)
    assert data == ['26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб.',
                    '03.07.2019 Перевод организации\nСчет **5560\n8221.37 USD',
                    '30.06.2018 Перевод организации\nСчет **6952 -> Счет **6702\n9824.07 USD',
                    '04.04.2019 Перевод со счета на счет\nСчет **8542 -> Счет **4188\n79114.93 USD',
                    '23.03.2019 Пополнение счета\nСчет **1160\n43318.34 руб.']


@pytest.mark.parametrize("test_input, expexted", [("Счет 35383033474447895560", "Счет **5560"), (
"Visa Platinum 1596837868705199", "Visa Platinum 1596 83** **** 5199")])

def test_encode_bill_info(test_input, expexted):
    assert encode_bill_info(test_input) == expexted