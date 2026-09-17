from sales_manager.analysis import analyze_sales


def test_total_records():
    """Verify that the total number of records is calculated."""
    rows = [
        {"id": "1", "product": "Mouse", "quantity": "2", "price": "20"},
        {"id": "2", "product": "Keyboard", "quantity": "3", "price": "35"},
    ]

    result = analyze_sales(rows)

    assert result["total_records"] == 2


def test_total_sales():
    """Verify that total sales are calculated correctly."""
    rows = [
        {"id": "1", "product": "Mouse", "quantity": "2", "price": "20"},
    ]

    result = analyze_sales(rows)

    assert result["total_sales"] == 40.0


def test_top_product():
    """Verify that the product with the highest sales is identified."""
    rows = [
        {"id": "1", "product": "Mouse", "quantity": "2", "price": "20"},
        {"id": "2", "product": "Laptop", "quantity": "2", "price": "500"},
    ]

    result = analyze_sales(rows)

    assert result["top_product"] == "Laptop"


def test_analysis_returns_dictionary():
    """Verify that the analysis function returns a dictionary."""
    rows = [
        {"id": "1", "product": "Mouse", "quantity": "2", "price": "20"},
    ]

    result = analyze_sales(rows)

    assert isinstance(result, dict)

