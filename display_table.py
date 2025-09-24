def display_table():
    """
    This function displays a simple table with 10 rows and 4 columns.
    """
    # Define table headers
    headers = ["Column 1", "Column 2", "Column 3", "Column 4"]

    # Generate sample data
    data = []
    for i in range(1, 11):
        row = [f"Row {i} Col 1", f"Row {i} Col 2", f"Row {i} Col 3", f"Row {i} Col 4"]
        data.append(row)

    # Determine the maximum width for each column
    column_widths = [len(header) for header in headers]
    for row in data:
        for i, cell in enumerate(row):
            if len(cell) > column_widths[i]:
                column_widths[i] = len(cell)

    # Print the header
    header_line = " | ".join(header.ljust(column_widths[i]) for i, header in enumerate(headers))
    print(header_line)
    print("-" * len(header_line))

    # Print the data rows
    for row in data:
        row_line = " | ".join(cell.ljust(column_widths[i]) for i, cell in enumerate(row))
        print(row_line)

if __name__ == "__main__":
    display_table()
