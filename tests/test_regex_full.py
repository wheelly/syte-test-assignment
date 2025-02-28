import pathlib

from regex_task import remove_rows_by_regex


def test_regex_remove_full(temp_tsv_file: str):
    """Tests the removal of rows by regex patterns."""

    # Get the name of the temporary CSV file since it's saved only in csv format after removal
    temp_csv_name = pathlib.Path(temp_tsv_file).with_suffix(".csv").as_posix()
    lines_before = count_lines_in_file(temp_tsv_file)

    try:
        remove_rows_by_regex(temp_tsv_file, temp_csv_name, "value1", "value5", "\t")
        lines_after = count_lines_in_file(temp_csv_name)
        assert lines_before > lines_after, f"Expected {lines_before} to be greater than {lines_after}"

    except Exception as e:
        assert False, f"An error occurred: {e}"
        
    finally:
        # Delete the temporary file
        pathlib.Path(temp_csv_name).unlink()


def count_lines_in_file(file_path: str) -> int:
    """Counts the number of lines in a file."""
    with open(file_path, 'r') as file:
        return sum(1 for _ in file)
