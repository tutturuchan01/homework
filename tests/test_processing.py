from src.processing import filter_by_state, sort_by_date


operations = [
    {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 2, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
]


def test_filter_by_state():
    assert len(filter_by_state(operations)) == 1

def test_sort_by_date():
    result = sort_by_date(operations)
    assert result[0]["date"] < result[1]["date"]

def test_sort_by_date_reverse():
    result = sort_by_date(operations, ascending=False)
    assert result[0]["date"] > result[1]["date"]
