import csv


def read_sales_file(path):
    """Read sales data from a CSV file."""
    with open(path, newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def save_sales_file(path, rows):
    """Save sales data to a CSV file."""
    if not rows:
        return

    with open(path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
