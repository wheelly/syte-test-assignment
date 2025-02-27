import os
import re

import click

from src.csv import CsvGetter


@click.command()
@click.option("--infile", type=os.PathLike, help='Input file csv')
@click.argument("out", type=os.PathLike)
@click.option("--pattern-eq", type=re.Pattern, default=r"knit", help="Column to copy from")
@click.option("--pattern-not", type=re.Pattern, default=r"jumpers", help="Column to copy from")
def remove_rows_by_regex(
    infile: os.PathLike,
    out: os.PathLike,
    pattern_eq: re.Pattern,
    pattern_not: re.Pattern
) -> None:
    """Transforms a CSV file to a TSV file."""
    with CsvGetter(in_file_path=infile, out_file_path=out) as df:
        for col in df.columns:
            # find the rows that match the pattern
            rows_eq = df[col].str.contains(pattern_eq, regex=True, flags=re.IGNORECASE)
            rows_not = df[col].str.contains(pattern_not, regex=True, flags=re.IGNORECASE)
            # drop rows that match pattern_eq and do not match pattern_not
            df = df[~(rows_eq & ~rows_not)]
