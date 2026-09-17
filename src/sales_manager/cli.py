from pathlib import Path

from .analysis import analyze_sales
from .cleaning import clean_sales_data
from .io import read_sales_file, save_sales_file


def run(input_path, output_path):
    """Run the sales data processing workflow."""
    rows = read_sales_file(input_path)
    cleaned_rows = clean_sales_data(rows)
    results = analyze_sales(cleaned_rows)
    save_sales_file(output_path, cleaned_rows)

    return results


def main():
    """Run the command-line application."""
    input_path = Path("data/raw/sales.csv")
    output_path = Path("data/output/clean_sales.csv")

    results = run(input_path, output_path)

    print("Smart Sales Data Manager")
    print("------------------------")
    print(f"Total records: {results['total_records']}")
    print(f"Total sales: {results['total_sales']}")
    print(f"Top product: {results['top_product']}")
    print(f"Result saved: {output_path}")


if __name__ == "__main__":
    main()
