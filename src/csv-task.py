import os

import click

from src.csv import CsvGetter


@click.command()
@click.option("--infile", type=os.PathLike, help='Input file csv')
@click.argument("out", type=os.PathLike)
@click.option("--column_source", type=str, default="search_price", help="Column to copy from")
@click.option("--column_target", type=str, default="price_edited", help="Column to copy to")
def transform_csv_task(infile: os.PathLike, out: os.PathLike, column_source: str, column_target: str) -> None:
    """Transforms a CSV file to a TSV file."""
    with CsvGetter(in_file_path=infile, out_file_path=out, sep="\t") as df:
        if column_source not in df.columns:
            raise ValueError(f"Column {column_source} not found in the file")
        df[column_source] = df[column_target]
