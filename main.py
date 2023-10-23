# import sys
# from csv_functions import load_csv, count_rows, sum_column, min_max_avg, shortest_longest_string
#
# if __name__ == "__main__":
#     if len(sys.argv) < 2:
#         print("Please provide a CSV filename as an argument.")
#         sys.exit(1)
#
#     filename = sys.argv[1]
#     try:
#         data = load_csv(filename)
#     except FileNotFoundError:
#         print(f"File {filename} not found")
#         sys.exit(2)
#
#     print(f"Number of rows: {count_rows(data)}")
#
#     col_index = 1
#     try:
#         print(f"Sum of column {col_index}: {sum_column(data, col_index)}")
#     except ValueError as e:
#         print(e)
#     try:
#         min_val, max_val, avg_val = min_max_avg(data, col_index)
#         print(f"Minimum value in column {col_index}: {min_val}")
#         print(f"Maximum value in column {col_index}: {max_val}")
#         print(f"Average value in column {col_index}: {avg_val}")
#     except ValueError as e:
#         print(e)
#
#     try:
#         shortest, longest = shortest_longest_string(data, col_index)
#         print(f"Shortest string in column {col_index}: {shortest}")
#         print(f"Longest string in column {col_index}: {longest}")
#     except ValueError as e:
#         print(e)
#
import sys
from csv_functions import load_csv, count_rows, sum_column, min_max_avg, shortest_longest_string


def display_menu():
    print("\nMenu:")
    print("1. Load CSV File")
    print("2. Display Number of Rows")
    print("3. Sum of a Column")
    print("4. Minimum, Maximum, and Average of a Column")
    print("5. Shortest and Longest String in a Column")
    print("6. Exit")


def load_data():
    filename = input("Enter the CSV filename: ")
    try:
        return load_csv(filename)
    except FileNotFoundError:
        print(f"File {filename} not found")
        return []


if __name__ == "__main__":
    data = []

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            data = load_data()
        elif choice == "2":
            if not data:
                print("Data not loaded. Please load a CSV file first.")
                continue
            print(f"Number of rows: {count_rows(data)}")
        elif choice in ["3", "4", "5"]:
            if not data:
                print("Data not loaded. Please load a CSV file first.")
                continue
            col_index = int(input("Enter column index: "))
            if choice == "3":
                try:
                    print(f"Sum of column {col_index}: {sum_column(data, col_index)}")
                except ValueError and IndexError as e:
                    print(e)
            elif choice == "4":
                try:
                    min_val, max_val, avg_val = min_max_avg(data, col_index)
                    print(f"Minimum value in column {col_index}: {min_val}")
                    print(f"Maximum value in column {col_index}: {max_val}")
                    print(f"Average value in column {col_index}: {avg_val}")
                except ValueError and IndexError as e:
                    print(e)
            elif choice == "5":
                try:
                    shortest, longest = shortest_longest_string(data, col_index)
                    print(f"Shortest string in column {col_index}: {shortest}")
                    print(f"Longest string in column {col_index}: {longest}")
                except ValueError as e:
                    print(e)
        elif choice == "6":
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")
