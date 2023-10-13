import sys
from csv_functions import load_csv, count_rows, sum_column, min_max_avg, shortest_longest_string

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a CSV filename as an argument.")
        sys.exit(1)

    filename = sys.argv[1]
    data = load_csv(filename)

    print(f"Number of rows: {count_rows(data)}")

    col_index = 1
    print(f"Sum of column {col_index}: {sum_column(data, col_index)}")
    min_val, max_val, avg_val = min_max_avg(data, col_index)
    print(f"Minimum value in column {col_index}: {min_val}")
    print(f"Maximum value in column {col_index}: {max_val}")
    print(f"Average value in column {col_index}: {avg_val}")

    shortest, longest = shortest_longest_string(data, col_index)
    print(f"Shortest string in column {col_index}: {shortest}")
    print(f"Longest string in column {col_index}: {longest}")
