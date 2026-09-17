from typing import Dict, List


def clean_sales_data(rows: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """Clean sales records by handling missing values and duplicates."""
    cleaned_rows = []
    seen = set()

    for row in rows:
        row_key = tuple(row.items())

        if row_key in seen:
            continue

        seen.add(row_key)

        cleaned_row = row.copy()

        if not cleaned_row["quantity"]:
            cleaned_row["quantity"] = "0"

        cleaned_rows.append(cleaned_row)

    return cleaned_rows


