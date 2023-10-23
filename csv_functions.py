import csv


def load_csv(file_or_filename):
    if isinstance(file_or_filename, (str, bytes)):
        try:
            file = open(file_or_filename, 'r')
        except FileNotFoundError:
            raise FileNotFoundError(f"File {file_or_filename} not found")

    else:
        file = file_or_filename

    reader = csv.reader(file, delimiter=',', skipinitialspace=True)

    data = [row for row in reader if len(row) > 0]

    if isinstance(file_or_filename, (str, bytes)):
        file.close()

    return data


def count_rows(data):
    return len(data) - 1


def sum_column(data, col_index):
    if col_index >= len(data[0]):
        raise IndexError(f"Column index {col_index} out of range")
    elif col_index <= 0:
        raise ValueError(f"Column index {col_index} must be greater than 0")

    total = 0
    for row in data[1:]:
        try:
            total += float(row[col_index])
        except ValueError:
            raise ValueError(f"Invalid value at column {col_index}: {row[col_index]}")

    assert total  # not empty

    return total


def min_max_avg(data, col_index):
    if col_index >= len(data[0]):
        raise IndexError(f"Column index {col_index} out of range")
    elif col_index <= 0:
        raise ValueError(f"Column index {col_index} must be greater than 0")

    values = []
    for row in data[1:]:
        values.append(float(row[col_index]))

    assert values  # not empty
    return min(values), max(values), sum(values) / len(values)


def shortest_longest_string(data, col_index):
    if col_index >= len(data[0]):
        raise IndexError(f"Column index {col_index} out of range")
    elif col_index < 0:
        raise ValueError(f"Column index {col_index} must be greater than 0")

    strings = []
    for row in data[1:]:
        if row[col_index] == "":
            continue
        elif not isinstance(row[col_index], str):
            raise ValueError(f"Invalid value at column {col_index}: {row[col_index]}")
        strings.append(row[col_index])
    shortest = min(strings, key=len)
    longest = max(strings, key=len)
    assert shortest  # not empty
    assert longest  # not empty
    return shortest, longest
