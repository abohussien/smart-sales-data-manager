import argparse
from pathlib import Path
from typing import Any, Dict, Union

from .analysis import analyze_sales
from .cleaning import clean_sales_data
from .io import read_sales_file, save_sales_file


def run(
    input_path: Union[str, Path], output_path: Union[str, Path]
) -> Dict[str, Any]:
    """Run the sales data processing workflow."""
    rows = read_sales_file(input_path)
    cleaned_rows = clean_sales_data(rows)
    results = analyze_sales(cleaned_rows)
    save_sales_file(output_path, cleaned_rows)

    return results


def main() -> None:
    """Run the command-line application."""
    parser = argparse.ArgumentParser(
        description="Clean and analyze sales CSV data."
    )

    parser.add_argument(
        "input",
        nargs="?",
        default="data/raw/sales.csv",
        help="Path to the input CSV file.",
    )

    parser.add_argument(
        "-o",
        "--output",
        default="data/output/clean_sales.csv",
        help="Path to the output CSV file.",
    )

    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    results = run(input_path, output_path)

    print("Smart Sales Data Manager")
    print("------------------------")
    print(f"Total records: {results['total_records']}")
    print(f"Total sales: {results['total_sales']}")
    print(f"Top product: {results['top_product']}")
    print(f"Result saved: {output_path}")


if __name__ == "__main__":
    main()