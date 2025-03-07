import re
from typing import Optional

import click
import pandas as pd

from csv_getter import CsvGetter


@click.command()
@click.option("--infile", required=True, type=click.Path(exists=True, dir_okay=False, readable=True), help="Input file csv")
@click.option("--out", required=True, type=click.Path(writable=True), help="Output file csv")
@click.option("--pattern-eq", type=str, default=r"knit", help="Column to copy from - default 'knit'")
@click.option("--pattern-not", type=str, default=r"jumpers", help="Column to copy from - default 'jumpers'")
def main(
    infile: str,
    out: str,
    pattern_eq: str,
    pattern_not: str
) -> None:
    remove_rows_by_regex(infile, out, pattern_eq, pattern_not)


def remove_rows_by_regex(
    infile: str,
    out: str,
    pattern_eq: str,
    pattern_not: str,
    sep: Optional[str] = ","
) -> pd.DataFrame:
    """Removes rows from a CSV file that match a pattern and do not match another pattern."""

    with CsvGetter(in_file_path=infile, out_file_path=out, sep=sep) as df:
        eq_re = re.compile(pattern_eq, re.IGNORECASE)
        not_re = re.compile(pattern_not, re.IGNORECASE)

        # Apply regex search across all columns
        mask_eq = df.map(lambda x: bool(eq_re.search(str(x))) if pd.notnull(x) else False)
        mask_not = df.map(lambda x: bool(not_re.search(str(x))) if pd.notnull(x) else False)

        # Create a boolean mask for rows to keep
        mask = ~(mask_eq.any(axis=1) & ~mask_not.any(axis=1))

        # Drop rows by mask in place
        df.drop(index=df[~mask].index, inplace=True)
        # Reset index in place
        df.reset_index(drop=True, inplace=True)
        # Everything must be inplace since we are in a context manager and this is the only way to save the changes
        # if we use new ref to df, it will not be saved into the file since CsvGetter.df will hold the old ref
        return df


if __name__ == "__main__":
    main()
