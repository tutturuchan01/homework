from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(operations):
    assert len(filter_by_state(operations)) == 1


def test_sort_by_date(operations):
    result = sort_by_date(operations)

    assert result[0]["date"] < result[1]["date"]


def test_sort_by_date_reverse(operations):
    result = sort_by_date(
        operations,
        ascending=False,
    )

    assert result[0]["date"] > result[1]["date"]

