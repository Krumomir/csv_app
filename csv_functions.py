import csv


def load_csv(file_or_filename):
    if isinstance(file_or_filename, (str, bytes)):
        file = open(file_or_filename, 'r')
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
    total = 0
    for row in data:
        try:
            total += float(row[col_index])
        except ValueError:
            raise ValueError(f"Invalid value at column {col_index}: {row[col_index]}")

    assert total  # not empty

    return total


def min_max_avg(data, col_index):
    values = []
    for row in data[1:]:
        values.append(float(row[col_index]))

    assert values  # not empty
    return min(values), max(values), sum(values) / len(values)


def shortest_longest_string(data, col_index):
    strings = []
    for row in data[1:]:
        strings.append(row[col_index])
    shortest = min(strings, key=len)
    longest = max(strings, key=len)
    assert shortest  # not empty
    assert longest  # not empty
    return shortest, longest
