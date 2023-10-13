import pytest
from io import StringIO

from csv_functions import load_csv, count_rows, sum_column, min_max_avg, shortest_longest_string

CSV_CONTENT = """name,age,salary
Alice,28,55000.5
Bob,24,49000.3
Charlie,30,60000.8
"""

EMPTY_CSV = """"""
SINGLE_COLUMN_CSV = """name
Alice
Bob
Charlie
"""


def test_empty_csv():
    csv_file = StringIO(EMPTY_CSV)
    data = load_csv(csv_file)
    assert count_rows(data) == -1


def test_single_column_csv():
    csv_file = StringIO(SINGLE_COLUMN_CSV)
    data = load_csv(csv_file)
    assert count_rows(data) == 3
    assert shortest_longest_string(data, 0) == ("Bob", "Charlie")


def test_invalid_column_index():
    csv_file = mock_csv_file()
    data = load_csv(csv_file)
    with pytest.raises(IndexError):
        sum_column(data, 5)


def test_non_numeric_sum():
    non_numeric_csv = """name,age
    Alice,twenty-eight
    Bob,twenty-four
    """
    csv_file = StringIO(non_numeric_csv)
    data = load_csv(csv_file)
    with pytest.raises(ValueError):
        sum_column(data, 1)


def test_min_max_avg_for_non_numeric():
    csv_file = StringIO(SINGLE_COLUMN_CSV)
    data = load_csv(csv_file)
    with pytest.raises(ValueError):
        min_max_avg(data, 0)


def mock_csv_file():
    return StringIO(CSV_CONTENT)


def test_load_csv():
    csv_file = mock_csv_file()
    data = load_csv(csv_file)
    assert len(data) == 4  # 3 data rows + 1 header
    assert data[1] == ["Alice", "28", "55000.5"]


def test_count_rows():
    csv_file = mock_csv_file()
    data = load_csv(csv_file)
    assert count_rows(data) == 3


def test_sum_column():
    csv_file = mock_csv_file()
    data = load_csv(csv_file)
    assert sum_column(data, 1) == 82  # Sum of ages
    assert sum_column(data, 2) == 164001.6  # Sum of salaries


def test_min_max_avg():
    csv_file = mock_csv_file()
    data = load_csv(csv_file)
    min_val, max_val, avg_val = min_max_avg(data, 1)  # Ages
    assert min_val == 24
    assert max_val == 30
    assert avg_val == 27.333333333333332


def test_shortest_longest_string():
    csv_file = mock_csv_file()
    data = load_csv(csv_file)
    shortest, longest = shortest_longest_string(data, 0)  # Names
    assert shortest == "Bob"
    assert longest == "Charlie"
