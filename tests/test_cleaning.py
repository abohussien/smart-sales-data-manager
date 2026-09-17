from sales_manager.cleaning import clean_sales_data


def test_remove_duplicates():
    """Verify that duplicate records are removed."""
    rows = [
        {"id": "1", "product": "Mouse", "quantity": "2", "price": "20"},
        {"id": "1", "product": "Mouse", "quantity": "2", "price": "20"},
    ]

    result = clean_sales_data(rows)

    assert len(result) == 1


def test_handle_missing_quantity():
    """Verify that missing quantity is replaced with zero."""
    rows = [
        {"id": "1", "product": "Mouse", "quantity": "", "price": "20"},
    ]

    result = clean_sales_data(rows)

    assert result[0]["quantity"] == "0"


def test_keep_valid_quantity():
    """Verify that a valid quantity remains unchanged."""
    rows = [
        {"id": "1", "product": "Mouse", "quantity": "5", "price": "20"},
    ]

    result = clean_sales_data(rows)

    assert result[0]["quantity"] == "5"


def test_keep_unique_rows():
    """Verify that unique records are preserved."""
    rows = [
        {"id": "1", "product": "Mouse", "quantity": "2", "price": "20"},
        {"id": "2", "product": "Keyboard", "quantity": "3", "price": "35"},
    ]

    result = clean_sales_data(rows)

    assert len(result) == 2


def test_clean_sales_data_returns_list():
    """Verify that the cleaning function returns a list."""
    rows = [
        {"id": "1", "product": "Mouse", "quantity": "2", "price": "20"},
    ]

    result = clean_sales_data(rows)

    assert isinstance(result, list)
