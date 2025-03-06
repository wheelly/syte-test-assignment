import logging
import pathlib
from traceback import TracebackException
from types import TracebackType
from typing import Optional

import pandas as pd

logger = logging.getLogger(__name__)
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)


class CsvGetter:
    """Helper class for CSV files."""

    def __init__(
            self, in_file_path: str, out_file_path: Optional[str] = None, sep: str = ","):
        """
            Initializes the CsvGetter.
            :param in_file_path: The path to the input file.
            :param out_file_path: The path to the output file.
            :param sep: The separator for the CSV/TSV file. Default is CSV
        """
        self.in_file_path = in_file_path
        self.out_file_path = out_file_path if out_file_path else pathlib.Path(self.in_file_path).with_suffix(".csv")
        self.sep = sep

    def __enter__(self) -> pd.DataFrame:
        """Enters the context manager and reads cvs/tsv file into PandaFrame."""
        self.df = pd.read_csv(self.in_file_path, sep=self.sep)
        logger.info(f"Opening CSV file, records: {len(self.df)}")
        return self.df

    def __exit__(self, exc_type: BaseException, exc_value: TracebackException, exc_traceback: TracebackType):
        """Exits the context manager and saves the file to CSV."""
        if exc_type:
            logger.error(f"An error occurred: {exc_value}")
            return
        logger.info(f"Saving CSV file, records: {len(self.df)}")
        self.df.to_csv(self.out_file_path, index=False)
