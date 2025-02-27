import os

from src.csv import CsvGetter


def convert_tsv_to_csv(file_path: os.PathLike) -> None:
    """Converts a TSV file to a CSV file."""
    with CsvGetter(file_path, sep="\t"):
        pass
