from typing import Optional

import click

from csv_getter import CsvGetter


@click.command()
@click.option("--infile", required=True, type=click.Path(exists=True, dir_okay=False, readable=True), help="Input file tsv")
@click.option("--out", type=click.Path(writable=True), help="Output file csv")
def main(
    infile: str,
    out: str,
) -> None:
    convert_tsv_to_csv(infile, out)


def convert_tsv_to_csv(infile: str, out: Optional[str] = None) -> None:
    """Converts a TSV file to a CSV file."""
    with CsvGetter(infile, out_file_path=out, sep="\t"):
        pass


if __name__ == "__main__":
    main()
