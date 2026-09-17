from sales_manager.io import read_sales_file, save_sales_file


def test_read_sales_file(tmp_path):
    """Verify that sales data can be read from a CSV file."""
    file_path = tmp_path / "sales.csv"

    file_path.write_text(
        "id,product,quantity,price\n"
        "1,Mouse,2,20\n",
        encoding="utf-8",
    )

    result = read_sales_file(file_path)

    assert len(result) == 1


def test_read_sales_file_returns_rows(tmp_path):
    """Verify that CSV rows contain the expected data."""
    file_path = tmp_path / "sales.csv"

    file_path.write_text(
        "id,product,quantity,price\n"
        "1,Mouse,2,20\n",
        encoding="utf-8",
    )

    result = read_sales_file(file_path)

    assert result[0]["product"] == "Mouse"


def test_save_sales_file(tmp_path):
    """Verify that sales data can be saved to a CSV file."""
    file_path = tmp_path / "sales.csv"

    rows = [
        {"id": "1", "product": "Mouse", "quantity": "2", "price": "20"},
    ]

    save_sales_file(file_path, rows)

    assert file_path.exists()


def test_saved_file_contains_header(tmp_path):
    """Verify that the saved CSV file contains a header."""
    file_path = tmp_path / "sales.csv"

    rows = [
        {"id": "1", "product": "Mouse", "quantity": "2", "price": "20"},
    ]

    save_sales_file(file_path, rows)

    content = file_path.read_text(encoding="utf-8")

    assert "id,product,quantity,price" in content
