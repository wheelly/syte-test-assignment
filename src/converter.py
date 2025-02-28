from csv_getter import CsvGetter


def convert_tsv_to_csv(file_path: str) -> None:
    """Converts a TSV file to a CSV file."""
    with CsvGetter(file_path, sep="\t"):
        pass
