from typing import Any, Dict, List


def analyze_sales(rows: List[Dict[str, str]]) -> Dict[str, Any]:
    """Analyze cleaned sales records."""
    total_sales = 0
    product_sales = {}

    for row in rows:
        quantity = int(row["quantity"])
        price = float(row["price"])
        sale_value = quantity * price

        total_sales += sale_value

        product = row["product"]
        product_sales[product] = (
            product_sales.get(product, 0) + sale_value
        )

    top_product = max(product_sales, key=product_sales.get)

    return {
        "total_records": len(rows),
        "total_sales": total_sales,
        "top_product": top_product,
    }
