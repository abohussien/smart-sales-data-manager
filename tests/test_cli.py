from sales_manager.cli import run


def test_run_workflow(tmp_path):
    """Verify that the complete sales processing workflow works."""
    input_path = tmp_path / "sales.csv"
    output_path = tmp_path / "clean_sales.csv"

    input_path.write_text(
        "id,product,quantity,price\n"
        "1,Mouse,2,20\n"
        "1,Mouse,2,20\n",
        encoding="utf-8",
    )

    result = run(input_path, output_path)

    assert result["total_records"] == 1


def test_output_file_created(tmp_path):
    """Verify that the workflow creates the output file."""
    input_path = tmp_path / "sales.csv"
    output_path = tmp_path / "clean_sales.csv"

    input_path.write_text(
        "id,product,quantity,price\n"
        "1,Mouse,2,20\n",
        encoding="utf-8",
    )

    run(input_path, output_path)

    assert output_path.exists()

