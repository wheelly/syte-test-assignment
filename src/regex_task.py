import re

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
    pattern_not: str
) -> pd.DataFrame:
    """Removes rows from a CSV file that match a pattern and do not match another pattern."""

    getter = CsvGetter(in_file_path=infile, out_file_path=out)
    with getter as df:
        eq_re = re.compile(pattern_eq, re.IGNORECASE)
        not_re = re.compile(pattern_not, re.IGNORECASE)

        # Apply regex search across all columns
        mask_eq = df.map(lambda x: bool(eq_re.search(str(x))) if pd.notnull(x) else False)
        mask_not = df.map(lambda x: bool(not_re.search(str(x))) if pd.notnull(x) else False)

        # Create a boolean mask for rows to keep
        mask = ~(mask_eq.any(axis=1) & ~mask_not.any(axis=1))

        # Apply the mask and reset the index
        new_df = df[mask].reset_index(drop=True)
        # now it's a new ref so must save it to the instance
        getter.df = new_df
        return new_df


if __name__ == "__main__":
    main()
