import click
import pandas as pd

from csv_getter import CsvGetter


@click.command()
@click.option("--infile", required=True, type=click.Path(exists=True, dir_okay=False, readable=True), help="Input file csv")
@click.option("--out", required=True, type=click.Path(writable=True), help="Output file csv")
@click.option("--column-source", type=str, default="search_price", help="Column to copy from")
@click.option("--column-target", type=str, default="price_edited", help="Column to copy to")
def main(
    infile: str,
    out: str,
    column_source: str,
    column_target: str
) -> None:
    transform_csv_task(infile, out, column_source, column_target)


def transform_csv_task(
    infile: str,
    out: str,
    column_source: str,
    column_target: str
) -> pd.DataFrame:
    """Adds a new column to a CSV file from the old one."""
    with CsvGetter(in_file_path=infile, out_file_path=out) as df:
        if column_source not in df.columns:
            raise ValueError(f"Column {column_source} not found in the file")
        df[column_target] = df[column_source].astype(float)
        # the same ref changed inside so return the same address
        return df


if __name__ == "__main__":
    main()
