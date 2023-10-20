import pytest

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


def mock_open_file_conditionally(mocker, content):
    mock_file = mocker.mock_open(read_data=content)

    def side_effect(filename, mode='r'):
        if filename == 'mocked_file.csv':
            return mock_file()
        else:
            raise FileNotFoundError
    mocker.patch('builtins.open', side_effect=side_effect)


def test_load_csv_with_filename(mocker):
    mock_open_file_conditionally(mocker, CSV_CONTENT)
    data = load_csv('mocked_file.csv')
    assert len(data) == 4
    assert data[1] == ["Alice", "28", "55000.5"]


def test_load_csv_with_invalid_filename(mocker):
    # Mock the open function to raise a FileNotFoundError
    mocker.patch('builtins.open', side_effect=FileNotFoundError)

    with pytest.raises(FileNotFoundError):
        load_csv("non_existent_file.csv")


def mock_open_file(mocker, content):
    mocker.patch('builtins.open', mocker.mock_open(read_data=content))
    return open('mocked_file.csv', 'r')


def test_load_csv(mocker):
    csv_file = mock_open_file(mocker, CSV_CONTENT)
    data = load_csv(csv_file)
    assert len(data) == 4
    assert data[1] == ["Alice", "28", "55000.5"]


def test_empty_csv(mocker):
    csv_file = mock_open_file(mocker, EMPTY_CSV)
    data = load_csv(csv_file)
    assert count_rows(data) == -1


def test_single_column_csv(mocker):
    csv_file = mock_open_file(mocker, SINGLE_COLUMN_CSV)
    data = load_csv(csv_file)
    assert count_rows(data) == 3
    assert shortest_longest_string(data, 0) == ("Bob", "Charlie")


def test_invalid_column_index(mocker):
    csv_file = mock_open_file(mocker, CSV_CONTENT)
    data = load_csv(csv_file)
    with pytest.raises(IndexError):
        sum_column(data, 5)


def test_non_numeric_sum(mocker):
    non_numeric_csv = """name,age
    Alice,twenty-eight
    Bob,twenty-four
    """
    csv_file = mock_open_file(mocker, non_numeric_csv)
    data = load_csv(csv_file)
    with pytest.raises(ValueError):
        sum_column(data, 1)


def test_min_max_avg_for_non_numeric(mocker):
    csv_file = mock_open_file(mocker, SINGLE_COLUMN_CSV)
    data = load_csv(csv_file)
    with pytest.raises(ValueError):
        min_max_avg(data, 0)


def test_count_rows(mocker):
    csv_file = mock_open_file(mocker, CSV_CONTENT)
    data = load_csv(csv_file)
    assert count_rows(data) == 3


def test_sum_column(mocker):
    csv_file = mock_open_file(mocker, CSV_CONTENT)
    data = load_csv(csv_file)
    assert sum_column(data, 1) == 82
    assert sum_column(data, 2) == 164001.6


def test_min_max_avg(mocker):
    csv_file = mock_open_file(mocker, CSV_CONTENT)
    data = load_csv(csv_file)
    min_val, max_val, avg_val = min_max_avg(data, 1)
    assert min_val == 24
    assert max_val == 30
    assert avg_val == 27.333333333333332


def test_shortest_longest_string(mocker):
    csv_file = mock_open_file(mocker, CSV_CONTENT)
    data = load_csv(csv_file)
    shortest, longest = shortest_longest_string(data, 0)
    assert shortest == "Bob"
    assert longest == "Charlie"