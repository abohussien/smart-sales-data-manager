def clean_sales_data(rows):
    """Clean sales records by handling missing values and duplicates."""
    cleaned_rows = []
    seen = set()

    for row in rows:
        row_key = tuple(row.items())

        if row_key in seen:
            continue

        seen.add(row_key)

        if not row["quantity"]:
            row["quantity"] = "0"

        cleaned_rows.append(row)

    return cleaned_rows

