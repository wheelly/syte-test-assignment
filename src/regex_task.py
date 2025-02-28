import re

import click
import pandas as pd

from csv_getter import CsvGetter

# type=click.Path(exists=True, dir_okay=False, readable=True)
# type=click.Path(writable=True),


@click.command()
@click.option("--infile", required=True, help="Input file csv")
@click.option("--out", required=True, help="Output file csv")
@click.option("--pattern-eq", type=str, default=r"knit", help="Column to copy from - default 'knit'")
@click.option("--pattern-not", type=str, default=r"jumpers", help="Column to copy from - default 'jumpers'")
def main(
    infile: str,
    out: str,
    pattern_eq: str,
    pattern_not: str
):
    remove_rows_by_regex(infile, out, pattern_eq, pattern_not)


def remove_rows_by_regex(
    infile: str,
    out: str,
    pattern_eq: str,
    pattern_not: str
) -> pd.DataFrame:
    """Removes rows from a CSV file that match a pattern and do not match another pattern."""
    with CsvGetter(in_file_path=infile, out_file_path=out) as df:
        eq_re = re.compile(pattern_eq, re.IGNORECASE)
        not_re = re.compile(pattern_not, re.IGNORECASE)
        for col in df.columns:
            # find the rows that match the pattern
            rows_eq = df[col].str.contains(eq_re, regex=True)
            rows_not = df[col].str.contains(not_re, regex=True)
            # drop rows that match pattern_eq and do not match pattern_not
            df = df[~(rows_eq & ~rows_not)]
        return df


if __name__ == "__main__":
    main()
